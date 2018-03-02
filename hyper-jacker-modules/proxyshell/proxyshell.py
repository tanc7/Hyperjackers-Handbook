#!/usr/bin/python
import os, sys, operator, socket, subprocess, threading,time
from termcolor import colored

# Chang Tan
# Lister Unlimited Cybersecurity Solutions, LLC.
# changtan@listerunlimited.com

### NEW DESIGN ###

# PUSH A BUTTON, COMPLETELY IDIOT-PROOF

#### OLD DESIGN ###
# Proxyshell is a shell that automatically creates SOCKS and HTTP proxies as you run commands through it.
#
# This is just a placeholder or a design diagram
#
# Every command typed into proxyshell, it itself is a python prompt, will be prepended with tsocks proxychains. Every command will run with full  privileges.
#
# Certain commands like SSH will be run through tsocks proxyshell. It may not be a action the user actually wants.
#
# typing ADD HTTP-PROXY <target> automatically runs ncat against <target> to add a new ncat http proxy.
#
# typing ADD SOCKS-PROXY <target> will automatically runs ssh -NfD <port> <user>@<host> <ssh port> against target and makes the proxy accessible by proxyport.
#
# Okay, I need to think it over a little more. interactive GUI or command line that might just make the task suckier.

def popen_background(cmd): # leaves everything in a pipe so we display it when we want it to.
    p = subprocess.Popen(cmd,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True,executable='/bin/bash')
    o = p.stdout.read()

    return o
    # o = o.splitlines()
    # for line in o:
    #     line = str(line.encode('utf-8')).strip().rstrip()
    #     print line
    #
    # commands = cmd.splitlines()
    # for command in commands:
    #     command = str(command).rstrip().strip()
    #     print "COMMAND RUNNING IN BACKGROUND: ",command
    #     p = subprocess.Popen(command,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True,executable='/bin/bash')
    #     output = p.stdout.read()
    #     lines = output.splitlines()
    #     for line in lines:
    #         print str(line).strip().rstrip()
    #     # how to use.
    #     # if I want the value of x that is dug up from a different function in the background.
    #     # ip address = popen_background("Whatever")
    #     # print ip address. And it'll do it.
    # return output

def bash_cmd_background(cmd): # runs in FOREGROUND.
    commands = cmd.splitlines()
    print commands
    for command in commands:
        command = str(command).rstrip().strip()
        command = command + ' &'
        print "DEBUG: Command is running\r\n\t",command
        subprocess.call(command,shell=True,executable='/bin/bash')
    return
def bash_cmd(cmd): # runs in FOREGROUND.
    commands = cmd.splitlines()
    print commands
    for command in commands:
        command = str(command).rstrip().strip()

        print "DEBUG: Command is running\r\n\t",command
        subprocess.call(command,shell=True,executable='/bin/bash')
    return

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

    print "SET SSH PORT: ",ssh_port
    return ssh_port

def add_conf(conf_line):
    conf_file = "/etc/proxychains.conf"
    conf_line = conf_line.strip().rstrip()
    conf_line = '\r\n' + conf_line
    w = open(conf_file,'a+')
    w.write(conf_line)
    print "Wrote Line to /etc/proxychaijns.conf: ",conf_line
    w.close()
    return
def add_socks_ssh_dynamic():
    user = get_user()
    proxyhost = get_host()
    ssh_port = get_ssh_port()
    proxyport = get_proxyport()
    add_proxy_cmd = "sudo ssh -NfD {} {}@{} -p {}".format(
        str(proxyport),
        str(user),
        str(proxyhost),
        str(ssh_port)
    )
    conf_line = "socks5 0.0.0.0 {}".format(str(proxyport))
    bash_cmd(add_proxy_cmd)
    add_conf(conf_line)
    return

def quit():
    exit(0)
    return


def fastoptions(options):
    # options is a multi line string
    counter = 0
    options = options.splitlines()

    for option in options:
        print '\t',str(counter),'.\t',str(option.strip().rstrip())
        # counter or (option-selected) --> option

        counter += 1
    return
def get_proxyhost():
    proxyhost = str(raw_input("Enter the PROXYHOST (Foreign target IP used as proxy) or leave nothing so its yourself: "))
    if proxyhost == None or '':
        proxyhost = '127.0.0.1'
    return proxyhost
def add_http_proxy_ncat():
    proxyhost = get_proxyhost()
    proxyport = get_proxyport()
    cmd = "ncat --listen --proxy-type http {} {} &".format(str(proxyhost), str(proxyport))
    bash_cmd(cmd)
    conf_line = "http {} {}".format(str(proxyhost),str(proxyport))
    add_conf(conf_line)
    return

def view_proxy_table():
    #prints current proxies

    current_proxies = popen_background("cat /etc/proxychains.conf | egrep -i 'http|socks'")
    os.system('clear')
    print "Current Proxies\r\n",current_proxies
    return


def proxy_command():
    #prints current proxies

    current_proxies = popen_background("cat /etc/proxychains.conf | egrep -i 'http|socks'")
    os.system('clear')
    print "Current Proxies\r\n",current_proxies
    cmd = str(raw_input("Enter your command (sh and bash): "))
    cmd = cmd.strip().rstrip()
    proxified_cmd = str("""tsocks proxychains {} &""".format(str(cmd)))
    bash_cmd(proxified_cmd)
    print "Command '{}', running in background!".format(str(proxified_cmd))
    return

def reset_proxychains_conf():
    default_proxychains_conf = """dynamic_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000
socks4 127.0.0.1 9050""".rstrip().strip()

    w = open('/etc/proxychains.conf','w')
    w.write(default_proxychains_conf)
    w.close()

    bash_cmd('service tor restart')
    print "/etc/proxychains.conf has been reset and Tor has been restarted"
    # bash_cmd('cat /etc/proxychains.conf')

    return

def nikto_scan_http():
    os.system('clear')
    print "Selected: Nikto-Scanner"
    print "NOTE: Enter TARGET Host IPv4 address. so http://8.8.8.8 would be '8.8.8.8'"
    target = get_host()
    print "NOTE: Enter TARGET PORT"
    targetport = get_ssh_port()
    proxyhost = get_host()
    proxyport = get_proxyport()
    cmd = "nikto -host {} -port {} useproxy http://{}:{}".format(
        str(target),
        str(targetport),
        str(proxyhost),
        str(proxyport)
    )
    bash_cmd(cmd)

    return

def nmap_scan_http():
    print """
    WARNING: NMap Usage of HTTP Proxy Scans can only be done with HTTP PORTS! Through a HTTP Proxy!

    Here is a quickie overview:

    SOCKS proxies can send traffic ----> HTTP

    But!

    HTTP CANNOT ----> SOCKS proxies.

    If you are using both SOCKS AND HTTP proxies, you have to...\r\n\t1.Set to strict_chain and \r\n\t2.Enter all SOCKS first before HTTP proxies.\r\n\n\nFor that reason I restrict the scans to HTTP scripts!
    """
    target = get_host()
    print "Selected TARGET: ",target
    print "NOTE: You can enter a port range or list of ports like 80,81,8080,81,443"
    targetport = get_ssh_port()
    lscmd = "clear;ls /usr/share/nmap/scripts/http* >httppipe | cat <httppipe | awk -F '/' '{print $6}'"
    script_list_http_only = popen_background(lscmd)
    print "DEBUG: ",str(script_list_http_only)
    fastoptions(script_list_http_only)
    optchosen = int(raw_input("Enter a script CHOICE: "))
    options = script_list_http_only.splitlines()
    script_choice = options[optchosen]
    print "DEBUG, SELECTED: ",script_choice," TARGET: ",target," PORT: ",targetport

    cmd = """tsocks proxychains nmap -Pn --script={} {} -p {}""".format(str(script_choice),str(target),str(targetport))
    bash_cmd(cmd)
    return

def main():
    bash_cmd('clear')
    options = """Exit
    ADD SOCKS PROXY (Dynamic SSH Forwarding).
    ADD HTTP-PROXY. (NCat Listener)
    COMMAND. Run a Command through the proxychain.
    SCAN NIKTO (HTTP)
    SCAN NMAP (HTTP)
    ANY OTHER NMAP SCAN (SOCKS)
    """.strip().rstrip()
    static_commands = """
    STATIC COMMANDS:

    'clear' - Wipes the entire proxychains table, resets values to using Tor and Dynamic Chaining
    'list' - Shows the proxychains table
    """

    print static_commands
    fastoptions(options)
    optchosen = str(raw_input("Enter a option: "))
    if optchosen == '0':
        quit()
    elif optchosen == '1':
        add_socks_ssh_dynamic()
        main()
    elif optchosen == '2':
        add_http_proxy_ncat()
        main()
    elif optchosen == '3':
        proxy_command()
    elif optchosen == '4':
        nikto_scan_http()
        main()
    elif optchosen == '5':
        nmap_scan_http()
        main()
    elif optchosen == '6':
        any_nmap_scan_socks()
        main()
    elif optchosen == 'clear':
        reset_proxychains_conf()
        main()
    elif optchosen == 'list':
        view_proxy_table()
        time.sleep(5)
        main()
    else:
        main()
    return
main()
