# Performing your first network-based Hyper-Jump to attack people in a wireless network


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

Remember with the routing rule we added before we should be able to only percieve a 255 host range on 10.81.24.0/24. To add more subnets we need to alter the netmask part of the routing table. However I do not want to expose the VM to more hosts, potentially a very thick range of potential attackers. 


```
root@kali: 
```
