#!/bin/sh
SHELL=/bin/bash

#TAILSPIN
# Lister Unlimited Cybersecurity Solutions, LLC.
# Experiment WIP. Evade a attacker that knows part of your routing paths (in a multi NATed network)
# By initiating a full rotation of a entire subnet. And each device behind it. Giving it only one static point of entry
# useful for multi subnet implementations for a offensive focused red team.

# design

Kali (192.168.200.6) virbr1 (192.168.200.1)
Windows Server 2016 (172.16.84.9) virbr2 (172.16.84.1)
HOST Debian 9.3 (10.0.1.9) virbr0 (10.0.1.1)

Kali --------> Debian <-------- Windows
		^
		^
		NAT


		ATTACKER
When the HOST Debian gets attacked. The IPs switch entire NETWORKS and SUBNETS to prevent a repeated strike
from occuring behind the host

Done on command. The HOST detaches from the physical NAT and leaves a isolated instance behind.

Each GUEST will have their own autolaunching script to reroute, If timeout is hit, then the HOST will route
manually to it

The HOST has the encrypted register. Before spinning, each OS will encrypt their own part of the keys
And have it transferred to the HOST.

Each GUEST is responsible for reestablishing router for their devices. 
