#!/usr/bin/python
import os, sys, operator, socket, subprocess, threading,time
from termcolor import colored

# Chang Tan
# Lister Unlimited Cybersecurity Solutions, LLC.
# changtan@listerunlimited.com


    # this get commands require a lot of debugging. Apparently checking ' ' means if there is ANY  whitespaces in a string.
def get_proxyport():
    proxyport = str(raw_input("Enter the LOCAL PORT you are binding to the proxy: "))
    if proxyport == '' or None or '':
        proxyport = '1080'
    print "DEBUG SET PROXYPORT: ",proxyport
    return proxyport

def get_user():
    user = str(raw_input("Enter a USERNAME or leave blank to let it default as 'root' for login: "))
    if user == '' or None or '':
        user = 'root'

    return user

def get_host():
    host = str(raw_input("Enter HOST, either IPv4 Address or a URL: ")).strip().rstrip()
    if host == '' or None:
        print "Listen, I can't do shit with you without a HOST. Okay? Just enter the fucking host.",host
        get_host()
    return host

def get_ssh_port():
    ssh_port = str(raw_input("Enter SSH Port if its not 22 or leave blank: "))

    if ssh_port == None or '' or ' ':
        ssh_port = '22'

--
        print '\t',str(counter),'.\t',str(option.strip().rstrip())
        # counter or (option-selected) --> option

        counter += 1
    return
def get_proxyhost():
    proxyhost = str(raw_input("Enter the PROXYHOST (Foreign target IP used as proxy) or leave nothing so its yourself: "))
    if proxyhost == None or '':
        proxyhost = '127.0.0.1'
    return proxyhost
