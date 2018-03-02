#!/usr/bin/python

Hyperjacker SIEM is a threat management service optimized for PENETRATION TESTING, NOT IT administration.

Every SIEM, IDS, or IPS requires significant reconfiguration to be useful. Otherwise it's
a constant flood of useless info from their own exploits.

What matters to the attacker.

1. CIRT response team alerts
2. Counter forensics
3. Imminent collapse of routing nodes (caused by the Blue Team)
4. Sniffing our own packets to ensure our offensive data security
5. Validating our stealth techniques
6. Logging the lowest protocol layers to observe the "noise we generate" (we all do, you can't block certain things)
7. IMMEDIATE service analysis of enemy hosts
8. Detecting alert signatures of opposing team IDS/IPS
9. Detecting of specific commands being executed, like, FINGER, ROUTE DEL, NGREP, TCPKILL, STRINGS, VOLATILITY, EYEWITNESS, SNORT, SURICATA, NTOPNG, NDPIREADER, IFCONFIG, TSOCKS, PROXYCHAINS
10. Automatic passive network mapping to enumerate additional subnets
11. Automatic IDS flooders
12. automatic proxy installation on a pivot detected (NETWORK/SUBNET SWITCH, PACKET FORWARD COMMAND
13. persistently running autoexploitation modules that ARE PASSIVE and MATCH YOUR PRIVILEGE
14. periodic log backups and auto-cover your tracks
15. Automatic daemon dispatches (like launching a drone to scout ahead)
16. Immediate countermeasures followed with manually controlled options
17. Automatic privilege and service detection
18. Detection of SYSTEM privilege and auto killing firewalls and AV
All of this immediately invalidates nearly all cybersecurity solutions today.
19. On screen alerting of TARGET acquisition on YOU. NMAP, HOSTS, SET TARGET
20. Lower layer scans detection, ARP, PING, ETC.
21. The UFW or IPTables should escalate OPEN -------> More restricted
	NOT Restricteed ----> OPEN for one more device port on current firewalls
22. On a listening port request, it should auto-release firewall blocked ports

23. Daemon-Evade. Evade imminent destruction upon suspected deauth, kick, tcpkill, ufw, or iptables commands. Using a widely practiced tactic of Daemonization through subprocess forking. 80-90% chance of success.

To perform this you have to be user of DaemonContext, a python package that guarantees creations of UNIX DAEMONS. You are not daemonizing, but you "split into 2" and your daemon copy is daemonized. 

I did accidentally Daemonize myself from a botched attempt last December 

It's a very boring existence. 10 minutes of wandering around spewing senseless strings at myself. Since I realized I couldnt get my control back I pushed the power button.

It seems that event is accidental. Never intentionally performed. Never wanted to. Couldnt even type 'ls'

The daemon does what it does, repeat a simple task virtually undetectable (if it surives). Daemons have unique privileges and CAN run at a privilege where it is INVISIBLE to other Daemons and processes. CAN, not guaranteed!

So it's more like, "Split into a lifeless zombie" rather than "Be something really cool with horns". So don't get excited.
 
	NOTE: daemoncontext has received a major documentation update.
That means I need to relearn it. Faster hopefully.

But I remembered you need to give it a script so it can actually do real work.
And you need to set settings to allow the Daemon to persist.
And  settings or signals to kill the Daemon (it's a untouchable drain on resources otherwise)


Generally a system daemon like CRON does a much better job than any of us user created daemons. 


