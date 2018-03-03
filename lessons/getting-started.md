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

# Installation

# 
