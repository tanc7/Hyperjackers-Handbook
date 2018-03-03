# Prerequisites

Pretty much any new full-featured laptop you can buy with a dedicated video is capable of performing well enough in this class. We will be...

1. Installing Debian 9.3 as the primary HOST
2. Installing KVM as the primary hypervisor, as most hypervisors are in fact a form of Linux
3. Installing Windows 10 Education Edition as our Windows guest
4. Installing Kali Linux 2018.1 as our primary attack VM (our little realm called Coldharbour)
5. Using LUKS encrypted hard disk partitions
6. Run Docker containers as extremely secure and efficient instances to perform repetitive tasks such as password cracking. Without any noticeable loss in performance.

The reasons are simple

```
1. We need to utilize PCI-Pass-Through technology to allow near bare-metal performance of intensive tasks
2. We need security by Nested-Virtualization
3. We need a penetration testing distro
4. We need a efficient means of controlling the flow of forensically identifiable information
5. We need appropriate test-hubs before launching malware attacks
6. We need a suitable environment to perform the planemeld (NAT Routing between our attacker and our target's network)
```

# New topics you need to get familiar with, now

1. Programming in Python, JavaScript, interaction with PowerShell and assembly.
2. The Virtual Shell along with bash, shell, and Z-Shell
3. Linux (Debian Derivatives)
4. Root privileges, Ubuntu run-as-root, and Security Enhanced Linux
5. Virtualization and attacking/defending hypervisors
6. Basic Networking commands
7. route, ip route, Proxy ARP
8. Pivoting and proxifying as a combatant
9. Encryption, obfuscation, pluggable transports
10. Shadowsocks, OpenVPN, WireGuard, Stunnel
11. The perspective of CHFI Forensics, what it takes to make evidence forensically viable and how to taint the evidence


I expect a complete newbie in this to take up to a year. I focus on training you in the relevant subjects to focus on, not the stupid shit that joe-chucklefuck from Stack Overflow may have led you circles with.

And for the love of God, if I actually taught a class in this shithole called UNLV, and I found out you cited YouTube, I am going to fucking auto-fail you. Fuck YouTube and Dubstep Hacking Videos. Get that shit out of my classroom.

Put on your birth-control-goggles and get your ass to Barnes and Noble and read something. Better yet, get a copy of Learning Python the Hard Way. Do NOT go to school for this. They'll show you a bunch of boring assed illustrations in a meaningless textbook and give you a multiple choice exam on shit you'll never practice in real life.

You will code. Mark my words. You will write yourself a app. Not my dog-assed looking app (1 year after launch it looks like dog-ass). You will install frameworks and HATE JavaScript, the "language" that was written in 10 days, but you will be gleeful to hear of how many exploits it will enable you to perform.

As for Microsoft, you will damn them to hell for how many exploits to you crafted got passed around to each cybersecurity firm and ended up in their Windows Defender database. Microsuck, take this as a sign of respect.

Fuck you too VirusTotal.

# Coldharbour?

In the (now old) MMO Elder Scrolls Online, the Daedric Prince Molag Bal launched a full-scale invasion against the realm of Nirn and attempted to merge his domain of Coldharbour with the protagonist's realm. Like two planets smashing together.

Using chains launched from his end, to drag Nirn into Coldharbour.

Had Molag Bal succeeded, he would have been the ruler of two hells. Hell on earth (Nirn) and the hell on ColdHarbour.

The beauty of this story is that we will create our own Coldharbour, and due to our ownership of OUR side of the network, as it is OURS and not the target. We will rule our end together, we can dictate routing paths, and who gets what. We can control the physics of this portion making it completely inhospitable for any fool that tries to invade it and make it out alive. Simply with two things, routing, and iptables.


You do need to secure the network. There is a possibility that if  you were to get pwned instead, well you lose Coldharbour as well, as they have possession of your KVM hypervisor's credentials. They can spin up additional instances to hide in and control what you can see in your former domain.

Basically the only way to purge yourself of a retaliatory cyberattack is the full reinstallation of your machine, and completely overwritten with zeroes. But there are ways to evade that and still have active malware, called the shadow volume.

Just be careful. Linux malware is much easier to deliver and get executed than on the Windows side.

# Installation: Debian

Install Debian first. FYI there are two types of Debian distros

1. Free
2. Non-Free

Now this doesn't mean that Debian is for charge or anything. It just so happens, that the Linux community prefers to live their lives in some delusional unshackled paradise without "proprietary-drivers" forcing them to bend over to manufacturers like Intel or NVidia. Yeah, fight the power or some shit.

Well shit, if you can find me ONE LAPTOP that can abide by the Free concept of Linux driver support. Just name me, ONE, from Dell or something.

***Go get the damn non-free drivers image.***

```
https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/9.3.0-live+nonfree/amd64/iso-hybrid/debian-live-9.3.0-amd64-gnome+nonfree.iso
```
Otherwise you'll be punching holes in the wall figuring out why you don't have network access or even be able to see your network card. Because it requires Non-Free Drivers.

Alternatively, you can install Ubuntu where all of these problems are resolved. Except, of course, the rest  of the issues with Linux. And you gotta install your NVidia GPU drivers anyways.

I strongly advise keeping your laptop with a ethernet cable in there. At least ethernet cards are usually properly supported and working out of the box. Assuming you got the right image like above, then it should connect to the proper Debian repository and download the drivers to get your wireless drivers working.


# Installation: KVM

When you first boot up Debian, you'll probably get a massive paragraph of errors. We are going to have to fix them too. But for now check that it would support KVM.

Make a script.

```
echo '' > KVM-autoinstall.sh
chmod 755 KVM-autoinstall.sh
nano KVM-autoinstall.sh
```
Then make sure your network connection is on. Either that or ethernet.
```
#!/bin/sh
SHELL=/bin/bash

su
apt-get update && apt install -y qemu-kvm libvirt-clients libvirt-daemon-system
apt-get install -y libvirt-daemon virt-manager
```

To exit the editor in nano,

`CTRL X`

To run the script in the background

`screen -S kvminstaller`

And then

`sh KVM-autoinstall.sh`
This is going to take a while, lets get you started by getting you the images that you need.

`wget http://cdimage.kali.org/kali-2018.1/kali-linux-2018.1-amd64.iso`

And you need a version of Windows 10. You need either the Professional or the Education edition because they permit the use of Elevated Powershell for our experiments and can run Hyper-V, a Microsoft Hypervisor. The free Home edition of Windows 10 is a crippled POS made for tools.

For UNLV, there is a deal where you can enter your student account number and grab a copy.
`https://unlv.onthehub.com/WebStore/OfferingDetails.aspx?o=2ac6e973-189d-e511-9413-b8ca3a5db7a1`

Perfect. This is going to be our malware test host. Then you are going to realize how difficult it really is to land a shell. You see, 24/7 it is a ongoing arms race between malware developers and  Microsoft engineers. The only guaranteed way to actually land a shell is to...

`build your own RAT (remote access trojan)`

If you can't get it for free, you can always use the Home Edition but it will lack needed features like Hyper-V. You can still run everything with KVM as a hypervisor. I just personally don't like overpopulated internal pentest labs that others may potentially, be able to reach and turn against us.


*Note, as of right now, bunch of dipshits are watching my laptop screen right now talking about hacking and shit. See, fuck you UNLV, starbucks, and you, the other guy that wanted to pick a fight with me for using a CLI at a coffee shop (we're talking about months ago)*

# Installation: Any VM Guest on KVM

Generally with any VM Guest, you end up with a .iso file. Avoid the virtual box images, the VMware images. They're all worthless. We need to regular .iso images. The same ones used to make boot disks. You can load them from virt-manager `virt-manager` and clicking `File --> New Virtual Machine`.

Now this is where it gets weird. We are going to run the OS's regular installer. Within the context of KVM. It should have prompted you to make a qcow2 virtual hard disk. Do it and ensure that the size is about 100GB at least for each OS that you are planning to install. When it finishes installing it will reboot and act as if it was booting a real hard disk installation of the Windows install or whatever.

Don't worry. Your Debian and KVM will be just fine. The VM instance cannot see beyond it unless you permit it to (the hyperjump section of this course where we are going to network multiple VMs together). It actually thinks that it's maximum disk storage is 100GB. 
