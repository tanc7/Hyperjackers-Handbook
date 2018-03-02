functionsw

def error_handler(o):

    keywords = ['success',
        'fail',
        'fault',
        'unable',
        'error',
        'connected',
        'key',
        'deauth',
        'gw',
        'net',
        'mask',
        'face',
        'dev',
        'int',
        'mac',
        'exception',
        'failed',
        'operstate','
        'priority: 1',
        'priority: 2'
    ]
    for key in keywords:
        if re.search(key, o):
            # display it because its important
            sys.stdout.write(str(o))
            print str(o)
        else:
            pass
    w = open('./logfile.log', 'a+')
    w.write(o)
    w.close()
    return
def bash_cmd(cmd):
    #split commands into splitlines

    lines = cmd.splitlines()
    for line in lines:
            line = str(line.encode('utf-8')).strip().rstrip() + ' &'
            command = str(line)
            p = subprocess.call(command,shell=True,executable='/bin/bash',stderr=subprocess.PIPE,stdout=subprocess.PIPE)
            o = p.stdout.read()
            o = str(o.encode('utf-8'))

            error_handler(o)




    return
def popen_check(path): # runs cat on path, returns the string
    cmd = "cat {path}"
    string = subprocess.call(cmd,shell=True,executable='/bin/bash')
    string = str(string).strip().rstrip()
    return string
def add_new_net():

    cmd = """
    route add -net {subnet} netmask {netmask} gw {gwip} dev {device} metric 1
    """
    cmd2 = """
    ip route add {subnet} dev {device}
    """

    cmd3 = """

    """
    try:

        bash_cmd(cmd.strip().rstrip())
    except Exception:
        try:
            bash_cmd(cmd2.strip().rstrip())
        except Exception:
            bash_cmd(cmd3.strip().rstrip())

    return

def check_operstate(device):
    operstate = popen_check("/sys/class/net/{device}/operstate")
    operstate = str(operstate)
    if operstate == 'off': # device is OFF and failed to turn on
        operstate = red(operstate)
    elif operstate == 'dormant': #device is "dormant" or hanging
        operstate = yellow(operstate)
    else: # device is UP
        operstate = green(operstate)
    print "Operstate of {device} is {operstate}"

    return operstate
def add_new_gw():
    if 'wl' in device:
        method = 'wpa'
    elif 'en' in device:
        method = 'ethernet'
    elif 'vir' or 'vnet' in device:
        method = 'virtualbridge'
    elif 'dock' in device:
        method = 'docker'
    elif 'lo' in device
        method = 'critical-loopback'

    if method == 'critical-loopback':
        cmd = """
        rfkill unblock {device}
        ifconfig {device} up"""


        return
    if method == 'wpa':
        cmd = """

        cp -r {wpaconf} {wpaconf}_{device}.conf
        wpa_supplicant -i {device} -c {wpa_conf}_{device}.conf &

        """
        bash_cmd("""dhclient {device}""")
        operstate = check_operstate(device)

        if operstate == "up":
            pass # go right to activate firewalls
        else:
            add_new_net() # because clearly it didnt work. So we gotta do it again.
        bash_cmd(cmd)
        return
    if method == 'ethernet':
        active_subnets = check_subnets()

        spare_subnets_to_make = [
            '192.168.0.1',
            '10.0.0.1',
            '172.84.0.1'
        ]

        for ip in spare_subnets_to_make:
            if ip not in active_subnets: # not occupied subnet
                if ip in spare_subnets_to_make: # and also not a made subnet
                    # index = spare_subnets_to_make[ip]
                    sn = ip
                    gwip = str(ip).strip().rstrip()
                    nm = '255.255.255.0'

                    sn = sn.split('.')
                    sn = '{0}.{1}.{2}.0'.format(str(sn[0]),str(sn[1]),str(sn[2]))
                    sn = str(sn)
                    cmd = """
                    ifup {device}
                    ifconfig {device} {gwip}
                    route add default gw {gwip} dev {device} metric 1
                    route add -net {sn}
                    route add 172.16.84.0 netmask 255.255.255.0 gw {virgwip} dev virbr0 metric 1
                    """
                    bash_cmd(cmd)
                    spare_subnets_to_make.pop[ip] # rfemove it from the queue
                    active_subnets.push[ip] # push into occupied subnets  stack
            else:
                pass
        return
    if method == 'virtualbridge':
        cmd =
        bash_cmd(cmd)
        return
    return
def change_mac_set_dev_up(): # and bring device up
    cmd = """clear
    rfkill unblock all
    macchanger -m {workingmac} {device}
    macchanger -e {device}
    ifconfig {device} up
    ifconfig {device} {gwip}
"""
    bash_cmd(cmd)
    return
def set_iface_off():
    cmd = """
    killall wicd wpa_supplicant network-manager avahi
    airmon-ng check kill
    ifconfig {device} down
    macchanger -p {device}
    rm -rf /var/run/wpa_supplicant/*
    clear
    cd /var/run/avahi
    echo 'Possible Causes of Dysfunction'$(ls)
    """
    bash_cmd(cmd)
    return

def get_subnet():
def get_device():
def get_netmask():
def get_gwip():

def main(): #user options
    string = """
    What are you routing?

    A new gateway to a new network (new device)
    A new gateway to a occupied network
    A mimicked MAC Address WiFi device (impersonation or bruted keys with mac addr spoofing and maybe mdk3)
    A Proxy ARP Ethernet --> Wifi
    Proxychains (Remote-evasion and recon)
    Shifting IP subnets to perform lateral movement in a penetration test
    Adding a hidden interface
    Attempting to merge your network offensively into another's wireless network (a 'invasion')
    In a emergency and need to escape. (Generate a distraction, scramble access point, restealth)
    """

    strings = string.splitlines()
    index = 0
    for line in strings:

        line = strings[index]
        line = str(line.encode('utf-8')).strip().rstrip()
        index += 1
        print str('#'+index+'\t'), line

    optchoice = int(raw_input("Enter a choice: "))

    if optchoice == 0:

    elif optchoice == 1:

    else
        main()
    return
main()
