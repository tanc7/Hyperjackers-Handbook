# Effective use of NESSUS

it is a misconception that NMap is meant to "scan for vulnerabilities". Nmap is a PORT-SCANNER, not a VULNERABILITY SCANNER, however with the correct configuration and scripts, it may be used to TEST for vulnerabilities.

If I were to type

```nmap <target> -p 1-6000```

All it wouldl do is which ports between 1 to 6000 are open. There is no checking for vulnerabilities. Here is a quick command that'll let you test for vulnerabilities but please be aware we have much better options in 2018.

```tsocks proxychains nmap --script=exploit <target> -p 1-12000```

# Introducing Nessus, a actual vulnerability scanner


Nessus, along with OpenVAS are among the two top-cited vulnerability scanners. Now personally, I use Nessus community edition and as a free package it can

1. Check for Shadowbrokers vulnerabilities (that is WannaCry and EternalRomance)
2. Check for SPECTRE AND MELTDOWN, I am assuming its due to public concern and consideration
3. Directly interface with your Metasploit Nightly / Metasploit Community Edition, which is also free
4. It can scan through isolated subnets if run locally, breaking past any local NAT firewall rules. This is done WITHOUT requiring pivoting.

This makes it amazingly powerful as a penetration testing tool and it should be the first thing to grab. By default the scans are NOT instrusive and must be configured to perform more detailed scans. This also helps "cover your ass" because if there is anything I can tell you about some pentest competition at Black Hat or DEFCON, is that many of the testing box has buckled repeatedly from nonstop nmap scans, locking out legit pentesters from ever interacting with it to claim the prize.

Now, Nessus / Tenable has a really confusing webpage but here is the link to get your community edition. Install it on your HOST, the Debian install and memorize what IP it is, from the Kali attacker perspective.

`https://www.tenable.com/downloads/nessus`

Now start Nessusd

```service nessusd restart```

And check that there is a HTTP service running on port 8834

```netstat -antp | grep 8834```

The login page is located at ```https://0.0.0.0:8834``` or ```https://localhost:8834```

You were asked previously to create a MASTER PASSWORD to unlock the database and from that page you can add a user (NOT A ROOT USER HOPEFULLY). Once you enter the Browser GUI. you can checkout the scans you can run there, OR, you can run msfconsole


```
msfdb init
msfdb start
msfconsole
load nessus
nessus_connect ctlister:PASSWORD@root@localhost:8834 ssl_verify
```

The functions of ```nessus_scan_launch``` is the exact same thing as making a new scan in the web GUI and running it. Be sure to heavily research the syntax of the msf --> nessus console

Now, we are focusing on importing the results of the scan into metasploit so we can actually combine them with exploits or further investigate suspected vulnerabilities. 

First, list all completed scans ```nessus_scan_list -c```. Find a completed scan's UUID and then run ```nessus_db_import <UUID>```, this will import the results of the scan and all of the hosts into your current database. If your workspace is 'default' like mine, and forgot to change it, then run in msfconsole `workspace -r default nessus` to rename the database to 'nessus' and switch to it.

