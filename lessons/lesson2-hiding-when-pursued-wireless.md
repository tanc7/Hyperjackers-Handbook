# Background

I primarily am certified in the attack and defense of Web Application Firewalls, and the breaching of Intrusion Detection and Prevention Systems.

![](https://github.com/tanc7/Hyperjackers-Handbook/raw/master/lessons/ids-ips-cert.png)
![](https://github.com/tanc7/Hyperjackers-Handbook/raw/master/lessons/sql-injection-cert.png)
![](https://github.com/tanc7/Hyperjackers-Handbook/raw/master/lessons/xss-cert.png)

I can attack on multiple vectors, but what do you do if ** you need to keep yourself on-the-run?**

# Evasion: Wireless Attacks

# Basic checklist of things you need to do

1. Change your MAC address
2. Change your hostname
3. Change your internal IP
4. Run commands through a proxy


# Change your MAC address

For most Linux installations, you are able to use macchanger to swap your device MAC address

```apt-get update && apt-get install -y macchanger```

```ifdown <interface> && macchanger -r -b && rfkill unblock all && ifup <interface> 10.81.24.199```

Sometimes it doesn't work, because its a driver issue, but this is really important it is one of the few forensically identifiable things about you.

# Change your hostname

Before you go back online, as the act of bringing wireless card to change your MAC address has disconnected you, you also need you change your hostname

```hostnamectl set-hostname <new name>```

This changes your hostname to something else. Think of a new name that doesn't spaces, but if you have to, you must escape the spaces. Keep the name short so it would, there is a bit-length to a acceptable hostname.

```hostnamectl set-hostname 'my\ shitty\ macbook'```

# Change your internal IP

First you need to connect back to the Wi-Fi Router you will get a new IP anyways overwriting the previous one.

Now I already did this, the change of my internal IP with the act ```ifup <interface> <internal IP>```

But when you reconnect, the DHCP service on the router or perhaps the RADIUS server has assigned a new IP. Change IP again anyways...

```ifconfig <interface> <new internal ip>```

Because you could be tracked by IT, and they can put you in a differing but working subnet for them to isolate and observe your activities.


# Fighting smarter not harder

In lesson 1, we covered the use proxychains, formerly we did not have to prepend proxychains with yet another command 'tsocks' because it would work on its own. However recently, proxychains got bugged and required tsocks to properly proxify your connections.

We will use tsocks-proxychains to interact with a 2nd machine without a trace of info. There are two types of proxies... that VIABLE for penetration testing. There is a ARP proxy but its used for something else.

1. SOCKS

2. HTTP

Generally, you want to stick with the SOCKS proxy except for web applications that the HTTP proxy would excel at.

You can make a SOCKS proxy in many ways, like rpivot, or msfconsole which contains own enhanced SOCKS4A proxy (that can do basic DNS resolution), but the most commonly available proxy generator is SSH.

```ssh -NfD <proxy port> <target proxy> -p <ssh port>```

You also must add this to your configuration file

```echo 'socks4 127.0.0.1 1080` >> /etc/proxychains.conf```

If I were to type,

```ssh -NfD 1080 user@192.168.1.1 -p 22```

It performs the act of logging in with public keys to that IP, and then attaching a proxy relay in the background. If you were do


```tsocks proxychains nmap 8.8.8.8```

It will nmap 8.8.8.8 with the identity of 192.168.1.1 and not you, Mr. 192.168.1.20.

Now we do have other options, but tell me how you are going to install rpivot or msfconsole remotely on machines you didn't even get into yet...


# The HTTP Proxy Alternative


HTTP Proxies offer numerous advantages BUT, there are drawbacks.

1. The proxy target MUST have HTTP ports opened and LISTENING

2. It can only scan web applications or URLs. Nothing else! If you try to run a scan on a non HTTP port while running a HTTP proxy, it would either (a) fail and not return anything or (b) perform a regular scan.

3. NMap is a terrible user of HTTP proxies and it's ability to perform scans while proxified with proxychains is quite limited. We will switch to Nikto instead.

But we should make a script that at least, automates the usage of nmap's HTTP vulnerability scanning scripts. In total, there are over 568 scripts just for nmap, a old, antiquated but still kept up to date port-scanner that unlike the upcoming Flavor of the Month apps on Kali Linux like Subgraph Vega or Arachni, nmap still remains useful because of one thing. "With the right parameters, you can perform a scan to detect ANYTHING with nmap." You can even breach firewalls with the right type of scan selected (preferably a ACK scan, or FIN scan) and the correct parameters to fool the WAF (Web Application Firewall) like fragmenting your packets BEFORE you launch the scan, altering the timing to fool the firewall's filters, or what we are doing right now, using a different server's headers as a identity because we know, we can get more information by impersonating a machine that the target actually TRUSTS.

First, lets find all of the http scanning scripts.
```
cd /usr/share/nmap/scripts
ls *http* >pipe
```

You're gonna see something like this. When you type ```cat pipe```

```
http-adobe-coldfusion-apsa1301.nse	http-open-proxy.nse
http-affiliate-id.nse			http-open-redirect.nse
http-apache-negotiation.nse		http-passwd.nse
http-apache-server-status.nse		http-phpmyadmin-dir-traversal.nse
http-aspnet-debug.nse			http-phpself-xss.nse
http-auth-finder.nse			http-php-version.nse
http-auth.nse				httppipe
http-avaya-ipoffice-users.nse		http-proxy-brute.nse
http-awstatstotals-exec.nse		http-put.nse
http-axis2-dir-traversal.nse		http-qnap-nas-info.nse
http-backup-finder.nse			http-referer-checker.nse
http-barracuda-dir-traversal.nse	http-rfi-spider.nse
http-brute.nse				http-robots.txt.nse
http-cakephp-version.nse		http-robtex-reverse-ip.nse
http-chrono.nse				http-robtex-shared-ns.nse
http-cisco-anyconnect.nse		http-server-header.nse
http-coldfusion-subzero.nse		http-shellshock.nse
http-comments-displayer.nse		http-sitemap-generator.nse
http-config-backup.nse			http-slowloris-check.nse
http-cors.nse				http-slowloris.nse
http-cross-domain-policy.nse		http-sql-injection.nse
http-csrf.nse				http-stored-xss.nse
http-date.nse				http-svn-enum.nse
http-default-accounts.nse		http-svn-info.nse
http-devframework.nse			http-title.nse
http-dlink-backdoor.nse			http-tplink-dir-traversal.nse
http-dombased-xss.nse			http-trace.nse
http-domino-enum-passwords.nse		http-traceroute.nse
http-drupal-enum.nse			http-unsafe-output-escaping.nse
http-drupal-enum-users.nse		http-useragent-tester.nse
http-enum.nse				http-userdir-enum.nse
http-errors.nse				http-vhosts.nse
http-exif-spider.nse			http-virustotal.nse
http-favicon.nse			http-vlcstreamer-ls.nse
http-feed.nse				http-vmware-path-vuln.nse
http-fetch.nse				http-vuln-cve2006-3392.nse
http-fileupload-exploiter.nse		http-vuln-cve2009-3960.nse
http-form-brute.nse			http-vuln-cve2010-0738.nse
http-form-fuzzer.nse			http-vuln-cve2010-2861.nse
http-frontpage-login.nse		http-vuln-cve2011-3192.nse
http-generator.nse			http-vuln-cve2011-3368.nse
http-git.nse				http-vuln-cve2012-1823.nse
http-gitweb-projects-enum.nse		http-vuln-cve2013-0156.nse
http-google-malware.nse			http-vuln-cve2013-6786.nse
http-grep.nse				http-vuln-cve2013-7091.nse
http-headers.nse			http-vuln-cve2014-2126.nse
http-huawei-hg5xx-vuln.nse		http-vuln-cve2014-2127.nse
http-icloud-findmyiphone.nse		http-vuln-cve2014-2128.nse
http-icloud-sendmsg.nse			http-vuln-cve2014-2129.nse
http-iis-short-name-brute.nse		http-vuln-cve2014-3704.nse
http-iis-webdav-vuln.nse		http-vuln-cve2014-8877.nse
http-internal-ip-disclosure.nse		http-vuln-cve2015-1427.nse
http-joomla-brute.nse			http-vuln-cve2015-1635.nse
http-litespeed-sourcecode-download.nse	http-vuln-misfortune-cookie.nse
http-ls.nse				http-vuln-wnr1000-creds.nse
http-majordomo2-dir-traversal.nse	http-waf-detect.nse
http-malware-host.nse			http-waf-fingerprint.nse
http-mcmp.nse				http-webdav-scan.nse
http-methods.nse			http-wordpress-brute.nse
http-method-tamper.nse			http-wordpress-enum.nse
http-mobileversion-checker.nse		http-wordpress-users.nse
http-ntlm-info.nse			http-xssed.nse
```
Now, what is a pipe? Well basically, it's a file that you can write-to or read-from. I am not sure why they call them pipes, probably because you can pipe it back and forth, like, read it into a file and then read it back to the screen... ```ls http* >pipe | /dev/stdout <read $pipe```.

Or something like ```service suricata restart | tail -f /var/log/suricata/fast.log | grep -i 'priority: 1' >intrusiondetectionsystem.log | read intrusiondetectionsystem.log > /dev/stdout```

That last command will give you a real-time display and properly log each alert moment. Usually alert priority: 1 is the most important portion, since only events such as a web application attack or your machine being actively compromised will show that kind of data. A aggressive nmap scan would usually appear as a priority: 2 instead.

Now, the script to auto-scan through EACH http type script using our proxychain that is still in /etc/proxychains.conf.

```
#!/bin/sh
shell=/bin/bash

webtargets='list_of_http_targets.log'
pipe='pipe'

for script in $(cat $pipe)
  do tsocks proxychains nmap --script=$script -p 80,443,8080,8081 -oX scanresults.xml -iL=$webtargets > /dev/null &
  done
```

So what exactly does the commands do?

1. It will run through your HTTP proxychains each script that was stored in the file called 'pipe' on nmap.
2. It targets only the relevant ports commonly known for HTTP (webserver) protocol. If you are hosting something, you are expected at least on most browsers, to host them on these four ports. Regardless of whether or not you can simply switch them to a new port like 65553. If you have a website, you better be hosting them on these four ports as thats what each browser expects, unless you intend to redirect them to a different one.
3. It selects the targets you specified in a  file called 'list_of_http_targets.log'.
4. It stores the data into a file in the same directory as where you ran it called './scanresults.xml', I chose XML because you can quickly import it into other frameworks such as msfconsole.
5. Any visually perceptible output is "piped" into "the void" referred to as /dev/null. There is a lot of debate on what /dev/null really is, but the important thing is to think of it as a black hole. Nothing is coming back out of it when it gets sucked in there. This will help you keep your head low and not be noticeable.
6. Finally, the '&' is important. This allows  you to run applications in the background giving shell access back to you. Now had we not followed #5, our work would be disrupted all the time because the scan results would be popping up all over the terminal. Not to mention that the cool-looking chain-icon thing from proxychains gets annoying eventually when you just want to get work done.

Verify that you have it running properly by ```ps aux | egrep -i nmap```

# Nikto: A scanner just for web applications

Another way of explaining what a web app is, is basically "any code on the web other than HTML or CSS that allows some degree of interactivity on a web page". JavaScript makes web-apps. PHP, Python-Django, and Ruby on RAILS are all web-apps. However, HTML and CSS are NOT web apps by themselves. Those last two are Markup Languages, much like Mark-Down, a crappy language invented by people that don't actually code (accountants from what I heard) that was forced on all of us poor saps on GitHub.


To interact or assess the security of a web app, you must send traffic that a web app expects to receive. That is certain not going to be the traffic we normally use on the aforementioned SOCKS proxies, which is more of something for SSH and Telnet, not HTTP.

When you run a scan using Nikto on a IP address such as 8.8.4.4:8080, we are address the web app like This

```https://8.8.4.4:8080/```

And not ```GET 8.8.4.4:8080``` which is a crappy console command for the same thing.

Often this difference is what could get you automatically banned by the web application firewall (CloudFlare especially, if you make too many requests without the expected User-Agents). It expects things like User-Agents (the browser you used to load a webpage, albeit other things qualify like web app vulnerability scanners.)

Many webservers are instinctively trained to perceive unnatural requests as a attempted attack. And if they come in high enough numbers, you get banned for half a hour and automatically logged and reported to the web domain's owner.

Non-web app requests, like ```ssh -i certificate.pem changtanlister@listerunlimited.com -p 22``` are commands that are for the BACK-END. Not the front-end which is where the web app is expected to operate at. They often are authenticated at much shorter thresholds before a ban occurs, because it's VERY UNUSUAL for someone visiting a webpage to be asking to access a back-end channel.

To run Nikto through proxychains, first go stick a suitable host with a HTTP proxy using ```ncat``` NOT ```nc``` or ```netcat```.

Now I am sorry that this lesson is so basic for you, since I have to get a ton of newbs up-to-speed on the hacking ordeal.
