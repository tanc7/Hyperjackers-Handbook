# Overview

```
Chang Tan
Lister Unlimited Cybersecurity Solutions, LLC.
changtan@listerunlimited.com
```
Hello class, in this section we will show you how to find a undetectable zero-day vulnerability. We will need another textbook to cite as a classic example but this section is designed to break you in in preparation of the outside source.

Now lets go over some terminology.


Zero Day Vulnerability (Zero-Day)
```
A zero day, is in simplest terms... a vulnerability discovered solely by the attacker and no one else.
```
Therefore NO ONE has a defense against the attack unless some security researcher eventually came across it. Often, when a zero-day is discovered by the researcher, the affected app's manufacturer is notified FIRST before public disclosure to the media. That way, once we find out, all we have as a malicious attacker is pre-patched vulnerabilities or a vulnerability where THERE IS a patch for it, but the potential target has NOT YET INSTALLED IT.

You have two choices.
1. Try your damndest to come up with a weaponized exploit and infect as many as you can or...
2. Reinvestigate the vulnerability to find something that you can exploit instead.

Fuzzer

```
A software that constantly transmits a pattern, usually a string with the intent of triggering a crash and ultimately, a starting point to find a zero day vulnerability. There are many type of fuzzers... meant to attack

1. SSH Protocols
2. FTP
3. In-system memory

```


NOP (Non-operator)

```
NOPs are in the simplest terms, characters or code that does NOTHING. However, when used to form a NOP SLED, it may assist in the guidance of the execution of your exploit by gently padding up the areas where the buffer may need "space to be filled", see below.
```

Debugger
```
Debuggers, if run on a binary (.exe or any other executable file) can help locate and figure out what is going on when we constantly test a single exploit. It may help in identifying and confirming a buffer overflow exploit. For example...

If I constantly blasted a program's SMTP socket with nothing but A's, and discover that part of the memory at the crash showed dnothing but A's, well hello there, we may have come across a potential buffer overflow exploit!
```

Buffer
```
A buffer is basically pre-allotted sections of memory that a program needs to fill in at a later moment. If I had a variable called 'firstName' but it's empty, that is a buffer to later on store a string. This is what we are targeting in a buffer overflow exploit.

Think of buffers as empty milk glasses.
```

Buffer Overflow
```
A buffer overflow exploit is when I intentionally inject string or code into the buffer, either by means of local injection right into the memory, or through a socket or port. With the right parameters, it will form the exploit in the empty spaces of the buffer, and hopefully, allow it to execute.

Think of me filling up two empty milk glasses. But I really suck at it, and I ended up filling up BOTH glasses by spilling it everywhere sloppily.

And yet somehow, despite me just sucking at pouring milk, the milk suddenly gets cursed, turns sour, and turned out it contains... ebolaids.
```

Heap Spray
```
Heap sprays are what would help in polishing a buffer overflow exploit but by no means should it ever be used to actually exploit someone.

Heap sprays are a sloppy tactic that will help you locate which sections of memory to focus on, as well as identifying 'bad characters' that are responsible for crashing the program instead of allowing smooth execution of your exploit.
```

Finding a buffer overflow and successfully weaponizing it will take months at most. This is not a easy task, but it can be done with a very basic understanding without having to know lower-level programming languages, but that last part my friends, is NOT a guarantee. If you know C, that'll really help right now.

All programs, are eventually turned into machine code from a `high level programming language` like Python to a `low level programming language` such as C and then into assembly and finally `binary machine code`, which is nothing more than a bunch of 1's and 0's that represent nothing more than 'on' and 'off'. You might have heard of `the transistor` and funny black and white movies of some guy out there eventually claiming it'll change the world. This is exactly what he is talking about.


Furthermore, we no longer live in the vacuum tube days and therefore, developers and engineers have implemented countermeasures to defeat our attempts in successfully crafting weaponized buffer overflow exploits. One method, ASLR or `Address Space Layer Randomization` will randomize the memory locations to make successfully developing a exploit much like hitting a moving target. This can be defeated using ROP or `Return Oriented Programming` which is very similar to `Reverse-Engineering` but the attacker is constantly fixated on the `output` or result of our attempts to exploit a vulnerability. This does, take a long-assed time however.

Another method is commonly used prior to ASLR, which was only utilized since Windows 7, is encryption and obfuscation. Which brings us two more terms, `encoders` and `stage encoders`.

Encoder
```
Encoders, from a penetration testing standpoint, does two things.

1. Aid in the execution of a exploit by encoding the payload in a scheme that our target's machine would understand like the x86/shitaka_ga_nai encoder
2. Help in avoiding immediate detection by the locally installed antivirus.

```
Encoding can be used to eliminate the 'bad byte' which may crash a potential payload had it not been identified earlier. Depending on language, architecture and platform, there are different types of bad bytes but the universal bad byte is '\x00' wshich you should immediately take care of.

However, encoders by themselves DO NOT make your malware undetectable. It must be combined with other methods.

Stage encoders
```
Is unique to the Metasploit-Framework. Formerly we discussed how to bypass latent antivirus software, we would load the payload in 'stages', like the booster of a rocket splitting off before the next section lights up and continues propelling a space shuttle.

Stage encoders perform the job of encoding the traffic of a msfvenom payload. This too will help avoid detection, but unfortunately, modern anti malware would still catch it. Not unless we do other things.
```

Signature
```
Each app or potential malware contains a signature. Or a profile. Anything on your machine can be returned a hash identifier value, which if it were to be malware, can be profiled and saved in a malware database that security software such as Windows Defender.


```
A common repository of malware signatures is VirusTotal.com often many new malware seen in the wild is submitted to VirusTotal and eventually the news that a certain sha256sum is actually malware will be dispatched to security firms such as Kaspersky, Symantec, and Microsoft.

Modern operating systems can be given a certificate and a signature if requested directly to Microsoft or Apple. If the application matches the signature, then it is pre-approved to execute. Unfortunately this has the side-effect that new software made by the open-source community will constantly be prevented from executing unless Run As Administrator.

Heuristics scanner
```
A heuristics scanner observes potential malware by monitoring the activities of it. Not the code itself.

1. Does it act like a virus?
2. Does it try to obtain SYSTEM or ROOT privileges?
3. Does it attempt to scan other processes for memory spaces and inject it with malware?
4. Does notepad.exe try to connect to the internet?
```

Heuristics scanners such as HitManPro are key to catching new malware variants in the wild. There are entire server-hypervisors, completely isolated in both network and media, that do nothing but observe potential malware that it may need to patch against.

Sandbox

```
What we just described above is a form of a sandbox.
```

However, new latent malware can detect the presence of a VM and from that, run further tests to conclude whether or not it got sandboxed. To ensure the infectiousness of the malware, the developers would try to avoid being sent to a sandbox and will lie dormant with periodic checks at later moments to double check.

At times, we have developed exploits that allow us to break out of VM's and Sandboxes, such as SPECTRE, MELTDOWN, and VENOM.


DO NOT confuse a IDS to a IPS. Both are critical to the security of a often-networked machine.
Intrusion Detection SYSTEM

```
When all other measures failed, even antivirus and web application firewalls, the malware may get logged in a intrusion detection system.
```
There are several types of intrusion detection systems, Host-based IDSs and Network-based IDSs. Host-based IDSs are more effective but more expensive to implement. All IDSes are NOISY as seen in the logs and will false-alert frequently.

Intrusion Prevention SYSTEM

```
The IPS is the first line of defense for a network, often placed either before or after the WAF.
```
fail2ban is a example of a IPS, on it's default configuration, it can initiate temporary bans for half a  hour against SSH brute forcing. With a bit of time invested, you can make fail2ban monitor ANY PORT and a HANDFUL of protocols including but not limited to, SSH, SMTP, SFTP, SCP, HTTP/HTTPS, etc. It can also be set with a iptables-hack to issue permanent bans.

Web Application Firewall

It's common for people to confuse a regular software firewall like ZoneAlarm with a proprietary WAF. But mainly...
```
WAF's are firewalls that protect web-applications
```
It's important to define web applications as well. Web applications are primary written in `JavaScript` or `Java` or `Ruby on RAILS` or `Python Django` or `PHP`. Web apps are critical to the interactivity of a website. But as they stand in the front-end for the user, it usually is the subject of attack for `Cross-Site Scripting` and `SQL Injection`. They are most likely to get `fuzzed`, or be hit by denial-of-service attacks, with the attacker knowing that the attack can negatively affect the server's back-end or reveal a potential exploit opportunity. It is also important to note that...

`Web Application attacks are the most diverse form of malicious hacking`

Due to the insane amount of frameworks being introduced every day such as `AngularJS`, `NodeJS`, `Web2Py`, and `Pyramid`, the opportunity for exploitation only continues to grow. That slick new

I just want to say, that developing a exploit using nothing but a debugger in a isolated environment will take quite a bit of time. It's the equivalent of writing code BLINDFOLDED. It's a non-stop cycle in implementing Return Oriented Programming, to find and locate a vulnerable section to use as a buffer, and a second buffer (usually) with adequate space to stick the actual payload into. Often, the original buffer overflow is used to create a `pointer` and `redirects` the execution into our `desired buffer`.


# Not finished. Need to add Offensive Security Penetration Testing book pages. 5:24pm
