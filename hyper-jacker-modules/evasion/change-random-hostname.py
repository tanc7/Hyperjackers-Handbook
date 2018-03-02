import random, re, os, sys, operator, socket, subprocess, threading, scapy, time, pexpect
from termcolor import colored
from os import mkfifo

toolkits_path = ".."
sys.path.append(toolkits_path)
import toolkits
from toolkits import red, green, yellow, cyan

red = toolkits.red
green = toolkits.green
yellow = toolkits.yellow
cyan = toolkits.cyan

# '/var/log/inpipe' = '/var/log/inpipe'
# outpipe = '/var/log/outpipe'

# people don';t want to admit it, but mkfifo is one of the dumbest and poorly documented modules in python.
# bash mkfifo wont accidentally get reclassified as strings! Which borks the funxtion of the pipe.
# or require level 9 in socery to properly conjure some motherfucking pipes without breaking it,.,

# okay. just remember.... using the python way....

# as soon as BOTH ENDS TOUCHs. thats (a) a writer (b) reader, the pipe is connected and has only 1 life. THe pipe is connected. Upon disconnect it must be DELETED
# command >{pipe} | read variable<${pipe} | cat variable >/dev/stdout
# Dollar signs are needed to refer to the valueq of a variable but it gets complicated.... because sometimes bash shell wont interpret properly
# We can use static pipe connector strings

pipe_right_new_var = ">"
pipe_left_old_var = "<$'var'"

# better to test out pipes in the bash shell before doing anything



def Popen_check(cmd):
    cmd = cmd + " &"
    p = subprocess.Popen(cmd,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True,executable='/bin/bash')
    o = p.stdout.read()
    o = str(o.encode('utf-8')).strip().rstrip()
    return o

def proper_pipe_read(inpipe, outpipe, kind): # readds f
    #stack = []

    if os.path.exists(outpipe):
        outpipe.unlink()
    # if not outpipe.exists:
    if not os.path.exists(outpipe):
        os.mkfifo('/var/log/outpipe')
    #w = open('hostnames.log','a+')
    if kind == 'hostname':
        w = open('hostnames.log','a+')
        r = w.readlines()
        stream = open('/var/log/inpipe', 'r')
        line = str(stream.readline()).strip().rstrip()
        print "HOSTNAME: ",line
        if line not in r:
            w.write(line)

        w.close()
    if kind == 'mac':
        x = open('mac_addrs.log','a+')
        r = x.readlines()
        stream = open('/var/log/inpipe','r')
        line = str(stream.readline()).strip().rstrip()
        print "BSSID: ",line
        if line not in r:
            x.write(line)

        x.close()
    return
def proper_pipe_write(line): # writes to a '/var/log/inpipe'

# this is precisely why I dumped pipes.
#AttributeError: 'module' object has no attribute 'inpipe'

    if os.path.exists('/var/log/inpipe'):
        os.path.inpipe.unlink()
    # if not '/var/log/inpipe'.exists:
    if not os.path.exists('/var/log/inpipe'):
        os.mkfifo('/var/log/inpipe')

    stream = open('/var/log/inpipe','a+')
    stream.write(line)

    return

def timer_thread():
    # outcomes = 'fuck you stack overflow'
    time.sleep(10)
    dogass = 'fuck you pexpect module'
    dogass = dogass.decode('utf-8') # decodes into UNICODE from UTF-8
    outcomes = dogass
    return outcomes
def pexpect_thread(cmd):
    encoding='utf-8'
    time = timer_thread()
    # #timesup = False
    thread = pexpect.spawn(cmd,timeout=300)
    # fout = 'airodump.log'
    # thread.logfile = fout
    # #thread.logfile_read = sys.stdout
    # thread.write()
    dogass = 'fuck you pexpect module'
    dogass = dogass.decode('utf-8')
    outcomes = thread.expect([pexpect.TIMEOUT, pexpect.EOF, dogass])
    # time.sleep(5)
    # outcomes = pexpect.TIMEOUT
    if(outcomes==0): # out of time
        print green("pexpect.TIMEOUT condition reached")
        results = thread.read()
        thread.terminate()
        w = open('./airodump.log')
        w.write(results)
        w.close()
        # logfile = thread.logfile
    elif(outcomes==1): # end of file error, just send another line to throw it into loop
        print yellow("pexpect.EOF conditioning reached")
        thread.sendline('\n')


    # elif(outcomes==2):
    #     results = thread.read()
    #     thread.terminate()
    #     w = open('./airodump.log')
    #     w.write(results)
    #     w.close()
    elif(outcomes==2):
        print green("Woo, the variable is dog-ass")
        print yellow("Thank you so much for wasting my time.")
        results = thread.read()
        thread.terminate()
        w = open('./airodump.log','a+')
        w.write(results)
        w.close()
    else:
        exception = thread.read()
        exception = str(exception.encode('utf-8')).strip().rstrip()
        print exception
        x = open('./exceptions_threading.log','a+')
        x.write(exception)
        x.close()

    return results, outcomes, exceptions

def bash_cmd(cmd):

    # bash paragraph interpreter
    cmd = cmd.splitlines()
    for command in cmd:
        command = str(command.encode('utf-8')).strip().rstrip()
        subprocess.call(command,shell=True,executable='/bin/bash')
    return

def pick_a_mac_address():
    mac_address_list = './mac_addrs.log'
    r = open(mac_address_list,'r')
    menu_interface_selection(lines, "Select a MAC Address")

    choice = int(raw_input("Select MAC by number: "))
    chosen_mac = stack[counter]
    print "Randomizing last two digits of MAC"

    array_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    array_numbers = [1,2,3,4,5,6,7,8,9,0]
    rand_letter = random.choice(string.array_letters)
    rand_number = random.randomint(integer.array_numbers)
    chars = chosen_mac.split('.')
    new_mac = "{}.{}.{}.{}.{}.{}{}".format(
        str(char[0]),
        str(char[1]),
        str(char[2]),
        str(char[3]),
        str(char[4]),
        str(rand_letter),
        str(rand_number)
    )

    print "Your new MAC address to change to is: {}".format(str(new_mac))
    time.sleep(1)
    change_mac_cmd = "macchanger -m {} {}".format(
        str(new_mac),
        str(device)
    )
    return change_mac_cmd
def change_identity():
    change_hostname_cmd = generate_random_hostname()
    change_mac_cmd = pick_a_mac_address()

    bash_cmd(change_hostname_cmd)
    # mon_iface = Popen_check("")
    stop_monitor_mode(mon_iface)
    bash_cmd(change_mac_cmd)
    conf = "/etc/wpa_supplicant/wpa_supplicant.conf"
    prep_cmd = """
    rfkill unblock all
    ifconfig {0} up
    wpa_supplicant -i {0} -c {1}
    """.format(
        str(device),
        str(conf)
    )
    bash_cmd(prep_cmd)

    return
def generate_random_hostname():
    hostname_list = "./hostnames.log"
    stack = []
    r = open(hostname_list,'r')
    lines = r.read()
    lines = lines.splitlines()
    for line in lines:
        hostname = str(line.encode('utf-8')).strip().rstrip()
        stack.append(hostname)

    random_hostname = random.choice(string.stack)
    random_hostname = random_hostname.replace(' ','-')
    print 'Random hostname selected: {}'.format(str(random_hostname))
    time.sleep(1)
    change_hostname_cmd = "hostnamectl set-hostname {}".format(str(random_hostname))

    return change_hostname_cmd


def stop_monitor_mode(mon_iface):
    bash_cmd("pkill airodump-ng")
    prep_cmd = """
    airmon-ng stop {}
    airmon-ng check kill
    killall wpa_supplicant network-manager wicd avahi
    rm -rf /var/run/wpa_supplicant/*
    rm -rf /var/run/avahi_daemon/*
    """.format(
        str(mon_iface)
    )
    bash_cmd(mon_iface)
    return
def switch_monitor_mode(device):
    cmd = "airmon-ng start {}".format(str(device))
    bash_cmd(cmd)
    mon_iface = Popen_check("iwconfig | grep -i mon | awk '{{print $1}}'")
    return mon_iface

def menu_interface_selection(mline_str, prompt):
    # This takes a multi-line string and prints out a interactive list
    lines = mline_str
    lines = lines.splitlines()
    stack = []
    for line in lines:
        line = str(line.encode('utf-8')).strip().rstrip()
        stack.append(line)
    counter = 0
    for line in stack:
        print str(counter)+'.\t',str(line)
    #    choice = int(raw_input("Select MAC by number: "))
        counter += 1
    print str(prompt)
    return line

def ten_second_airmon(device):
    mon_iface = switch_monitor_mode(device)
    os.system('clear')
    print "We are going idle for TEN seconds before coming back to read Airodump's log files, launching in 3 seconds"
    time.sleep(3)
    cmd = """airodump-ng --write-interval 1 --output-format csv --write airodump.log {}""".format(str(mon_iface))
    output = Popen_check(cmd)
    stop_monitor_mode(mon_iface)
    return output
def collect_new_mac_addrs(device):
    in_cmd = """airodump-ng --write-interval 1 --output-format csv --write airodump.log {}""".format(str(mon_iface))
    outfile = []
    kind = 'mac'

    mon_iface = switch_monitor_mode(device)

    stack = []

    r = open(excl_list,'r')
    stack = r.read()
    stack = stack.splitlines()
    for line in stack:
        line = str(line.encode('utf-8')).strip().rstrip()

    essid_stack = "cat airodump.log* | awk '{{print $1}}'"
    bash_cmd(essid_stack)
    time.sleep(10) # runs Airodump for ten seconds to collect the ESSIDs in area
    stop_monitor_mode(device)
    essid_stack = str(essid_stack.encode('utf-8')).replace(',','').strip().rstrip()
    new_essids = essid_stack.splitlines()
    for essid in new_essids:
        if essid not in stack:
            if re.search(essid, excl_list) == False:
                essid = str(essid.encode('utf-8')).strip().rstrip()
                print "Detected {}, adding it to the list"
                stack.append(essid)
        else:# do not add to list
            pass

    w = open(mac_addr_list,'a+')
    for essid in stack:
        w.write(essid)
        print "Wrote {} to physical save file: {}".format(
            str(essid),
            str(mac_addr_list)
        )

    w.close()

    # pushes the entire list into the new excl these essids stack
    bash_cmd("""cat {} >> {}""").format(
        str(mac_addr_list),
        str(excl_list)
    )

    print "Copied the contents of {} over to {} so you won't get double-counts of mac addresses".format(
        str(mac_addr_list),
        str(excl_list)
    )
    return mac_addr_list


def collect_new_hostnames(device):
    # excl_list = "./excluded_names.log" # any hostnames you dont want to adopt because they are too common
    # hostname_list = "./hostnames.log"
    # w = open(excl_list,'a+')
    # x = open(hostname_list,'a+')
    # # bash_cmd("echo '\n' >> {}".format(excl_list))
    # # bash_cmd("echo '\n' >> {}".format(hostname_list))
    # w.close()
    # x.close()
    interface_list = menu_interface_selection("ls /sys/class/net | grep -i wl", "Select a interface")
    # run airmon-ng on card
    raw_output = ten_second_airmon(device)
    lines = raw_output.splitlines()
    for line in lines:
        proper_pipe_write(line)

    return hostname_list
banner = """
    Macchanger Improved
    A needed makeover for a reknowned pentest tool

    'Automatically selects the CLOSEST non-conflicting MAC address by randomizing the last portion of the MAC'
    'Farms new real hostnames and MAC address ranges'
    'Swaps your hostname independently, allowing you to assume other identities or blend into corporate network routers and WDS systems, like UNLV-Secure, UNLV-Guest, or IGT-Gaming'

    Chang Tan
    Lister Unlimited Cybersecurity Solutions, LLC.
    changtan@listerunlimited.com
    Macchanger Improved is Part of the Hyperjacker's Toolkit
    Open-Source Penetration Testing Toolkits are NOT AVAILABLE FOR RESALE.
"""

print cyan(banner)
def main():

    menu = """Exit
    Farm new MAC addresses to impersonate
    Wi-Fi Hostname Farmer, Farm new Hostnames (Computer ID's) to impersonate
    Activate Switch Identity + MAC address
    View impersonatable names
    View impersonatable MAC addresses
    LAN Hostname Farmer, Farm locally connected Hostnames using NetDiscover"""

    print """
        (run python install.py)
        INSTALL. Install both the Python and Debian/Kali APT Prerequisites

        (read README.md)
        REQUIREMENTS. Mandatory required hardware to perform ARP Spoofing, Injection, and Packet Forgery
    """
    menu_interface_selection(menu, "Select a OPTION")

    choice = int(raw_input("Enter a integer to select a option: "))
    ifaces = Popen_check("ls /sys/class/net | grep -i wl")
    os.system('clear')
    menu_interface_selection(ifaces, "Select Interface")
    iface_selected = int(raw_input("Which device are you using?: "))

    device = ifaces[iface_selected]
    device = device.replace(',','').strip().rstrip()
    print "Device Selected: {}".format(str(device))

    hostname_list = "./hostnames.log"
    mac_address_list = './mac_addrs.log'
    if choice == 0:
        exit(0)
    elif choice == 1:
        collect_new_mac_addrs(device)
    elif choice == 2:
        collect_new_hostnames(device)
    elif choice == 3:
        change_identity()
    elif choice == 4:
        bash_cmd("cat {}".format(str(hostname_list)))
    elif choice == 5:
        bash_cmd("cat {}".format(str(mac_addr_list)))
    else:
        os.system('clear')
        print "INVALID OPTION"
        main()
    return
main()
