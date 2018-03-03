# Data Manipulation - Log Parsing

```
cat Read contents of file to the screen
read content<$pipe Read contents of a named pipe named variable pipe into a variable named 'content'
mkfifo $pipe Make a pipe named variable pipe
tail -f $file Read the last 3 lines to the screen and hold it OPEN, good for creating real-time displays with the bash console
awk -F '$fieldseperator' '{print $1}' While using a variable called $fieldseparator, separate each file by that, and then print the first column
egrep -i $searchterm Ignore-case (capital or lower) and search for anything that matches $searchterm
egrep -ix $s Do the same but now look for exact matches
egrep -iw $s Exact word
egrep -i $a | egrep -i $b From the search results of variable $a, look for whats in $b. Good for narrowing things down. 
egrep -i $search | egrep -vi '$ignore' Eliminate all appearances on the (per line) of $ignore out of the search results of $search
'' Single quotes tend to work better in separate or making linux interpret whats between them
'sentence "term"' Double quotes should be placed into single quotes to better clarify that whats between them is interpreted
```

# Cover your tracks

```
echo '' > dirt Completely replace everything in the file/pipe named 'dirt' with NOTHING. No spaces. Note the '>' means replace.
echo 'moredirt' >> dirt Append (add to) a line containing 'moredirt' into a pipe named dirt. Note the '>>' means APPEND or add a new line to.
echo '' > ~/bash_history Replace your bash history with nothing (wipe it)
rm -rf ~/.cache && rm -rf /root/.cache && /tmp/* Wipe your cache and all temporary files including your browsing history. Do this before you shut down the machine
ifconfig wlp60s0 192.168.10.5 Change your wireless interface's ip address to 192.168.10.5 from whatever it was before. **I highly recommend sticking with the same subnet. So if you are 192.168.10.135, you should restrict your IP choices to what is within the range of 192.168.10.0/24 and nothing else. Also, you might want to stick to the first 100 IP addresses.**
screen -S $new Make a new screen (a hidden terminal) named whatever $new contains
```

#within the new screen

```
CTRL + A + D
```

This backgrounds the screen. Hiding it from authorities. 
screen -r $new Goes back to the hidden screen

`mdk3` The forefather of all wireless exploitation toolkits today. Bit difficult to use so run mdk3 --fullhelp To look everything over and get some practice.

`tsocks proxychains`

`ssh -NfD $localport $user@$ip -p $sshport` Login via SSH at user@ipaddress through SSH port $sshport and then bind a SOCKS proxy onto it at 0.0.0.0:$localport
`echo 'socks 0.0.0.0 $localport' >> /etc/proxychains.conf` Add a new SOCKS proxy that you added in the previous step into the proxychain, remember, double pipe symbols! '>>', or else you will WIPE the file from a '>'

# Network interfaces manipulation commands

***Foreword: As the Linux Community continues to suck and releases more and more less popular and less adopted changes such as Predictable Network Interfaces, it may become astronomically more difficult to keep up with it. More and more drivers such as iwlwiki are still being left out in the cold and we may foresee a significant shift in what would be the king of pentest distros. It sure as hell ain't gonna be windows haha.***

Debian Only

Change your long-assed Predictable Network Interfaces name to a easier to work with name.

First make a file

```
echo '' > /etc/udev/rules.d/70-persistent-net.rules
nano /etc/udev/rules.d/70-persistent-net.rules
```
And for each interface that file add...

`ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="$macaddress", NAME="$newname", SUBSYSTEMS=="pci" `



Where $macaddress is the REAL mac address of the network card and $newname is whatever you want to call it, usually 'wlan0' 'wlan1' or 'eth0'. If you need to change it back to normal, then 

`macchanger -p $iface`


`hostnamectl set-hostname $hostname` Change your HOSTNAME without rebooting. This allows you to play the part of rogue access points. Because when they log into your fake hotspot they will find out your $HOSTNAME



# Simple & Relevant Scripting

How to make a working quickie script

```
#!/bin/sh
SHELL=/bin/bash
```
All your scripting shit


How to make a script executable

```chmod 755 $script.sh```


How to add a cronjob (starts at...)

`crontab -e`


How to start multiple python programs with a bash script wrapper

```
#!/bin/sh
SHELL=/bin/bash

/usr/bin/python program_1.py &
/usr/bin/python program_2.py &
/usr/bin/python program_3.py &

```
Then make this bash script a cronjob. Do not forget ampersands. 

How to make sure the crontab will work

`crontab -e`

And then add as the first UNCOMMENTED line


```
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/etc/init.d"
SHELL=/bin/bash
initpath=/etc/init.d
binpath=/usr/local/bin
```

Now everything in the directory /usr/local/bin with the permisssion '755' and properly referred in crontab will work. Always use full paths such as /bin/sh (shell scripts) /bin/bash (bash scripts) and /usr/bin/python (python files)

You can start the file as...


`@reboot /bin/sh $binpath/bash_wrapper_for_python_files.sh`


Which runs every reboot. Each cronjob as its called, will run PARALLEL to each other.


# Connectivity

How many wireless control programs do they have out there?

1. wpa_supplicant
2. wicd
3. network-manager

Do they all work? NO.

here is a force-wifi adapter to work at GUNPOINT script

```
#!/bin/sh
SHELL=/bin/bash

routef
for iface in $( ls /sys/class/net | grep -i 'wl' | grep -vi 'v' )
	do sudo ifconfig $iface down &
	sudo macchanger -p $iface &
	killall wpa_supplicant network-manager wicd parprouted avahi &
 	rm -rf /var/run/wpa_supplicant/* &
	airmon-ng check kill &
	cp -r /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/$iface.conf &
	done

for iface in $( ls /sys/class/net | grep -i 'wlan' )
	do ifconfig enp59s0 up
	sudo ifconfig $iface up
	iwconfig $iface mode managed
	iwconfig $iface power off
	iwconfig $iface txpower 30dbm
	iwconfig $iface commit
	rfkill unblock all
	macchanger --show
	echo '2'
	done
clear
virface=virbr0
virgw=192.168.122.1
sn=192.168.122.0
nm=255.255.255.0
metric=1
logvir=/var/log/virtualnet.log

rfkill unblock all &

sudo ifconfig $virface up $virgw &


echo '3'

workingmac=00:12:88:12:09:13
conf=/etc/wpa_supplicant/$iface.conf
wifilog=/var/log/wifilog.log
cd /sys/class/net

for iface in $( ls | grep -i 'wlan' )
	do rfkill unblock all
	sudo ifconfig $iface up
	chmod 777 /sys/class/net/$iface/*
	sleep 2
	clear
	echo $iface
	echo '4'
	cat /sys/class/net/$iface/operstate
	rfkill unblock all
	sleep 2
	sudo macchanger -m '00:12:88:12:09:13' $iface
	sleep 5
	sudo macchanger -e $iface
	rfkill unblock all
	sleep 2
	clear
	wpa_supplicant -i $iface -c $conf -dd -K | egrep -vi 'newlink|hexdump|key|mic' &
	dhclient $iface &
	done
```

# Why do they not work

Your network card manufacturer, or the Linux developer that borked the working copy is a asshole.

Also the needs of the Linux community has been pushed aside in favor of Windows 10 users. 

One day I would like to actually connect to public wifi without typing a million bajillion commands.

But until that moment all we got is some script I guess.


Oh yeah, this is primarily the reason why some dickhead towelhead at UNLV Student Union thinks that I am hacking. I am just trying to connect to the internet from your Linux incompatible wifi network dumbshit. 
