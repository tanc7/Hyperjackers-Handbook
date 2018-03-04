# Counter Forensics, or how a CHFI has a much harder time in holding the case together when prosecuting the bad guys

CHFI's or Computer Hacking Forensic Investigators, have to abide by several sources of authority in EVERY case, every INCIDENT, up to the court case that they are testifying in.

In that time, these investigators are required to prevent the contamination of the evidence, to keep track and serialize all noted pieces of collected forensically viable data, to draw conclusions from encrypted and obfuscated sources...


In Short, their job is much harder than ours. If our case, let's say involvement in a powerful cyber-crime syndicate was "contaminated" with scraps of evidence from their previous prosecuted case of a child pornography distributor were to be MIXED TOGETHER, due to the rushed implementation of a full hard disk wipe overwritten with zeroes, then the defense attorney can have the entire disk THROWN OUT.

Everything in that hard drive cannot be used as evidence. Because it brings into question to the lawyer, and to the judge, on how reliable that evidence is now, due to contamination.

This can be a serious advantage that we can leverage.

# Stringent requirements

I am certified by Cybrary in the introduction of Incident Response and Advanced Forensics. Cert #: SC-415cc1050-767d16

**Foreword: I Strongly suggest that you take and pass Max Alexander's class for Incident Response and Advanced Forensics to get a better understanding of what I am explaining. https://www.cybrary.it/skill-certification-course/incident-response-certification-training-course**

The typical workday for a CHFI on a case is extremely procedural. Make no mistake, CHFI's are very much the same as you and I, hackers, but they look at the activities of cybercrime and cyberwarfare in a much different perspective.

While we would look at methods of breaching a secure area or loopholes to flaunt the law, the CHFI is looking at our indicators and the trails we leave behind. This is why I emphasized constantly, the application of stealth tactics and covering your tracks. They all add up to this moment, where the "hideout" has been raided by LE and surrounded with police tape.

Using a warrant to exercise their authority, they will collect everything that you left behind. Your clothes, your old iPod (the really old one), your unused CDs, and especially your old mobile devices. They will often take out a fairly large "faraday bag", meant to seal off a device from outside communication and will analyze each device in a controlled environment by each hard disk sector. To prevent the reception of a remote signal meant to wipe the disk.

If you think that 'rm -rf' saved your ass, it's about to get dug up with their industry-standard forensics toolkits like Volatility Framework and Mandiant disk recovery apps. It will be reconstructed to the exact timestamp that you attempted to destroy the evidence. Within it, they could recover the .cache directories, the exact GPS latitude/longitude saved by Google Maps on your left behind Android phone, and every contact and text message in your contacts list. 

From the Blue Team's side, the CHFI and CIRT (Computer Incident Response Teams) have full access to the router logs to look into. This is not the exact copy of the data you sent, this is the data that they were able to discern the router has seen, including cleartext passwords, and is what they will build their case on. Remember this as it outlines the importance of applying encryption and obfuscation. 

There are things that not even a forensic investigator can decrypt, but one slip-up is all it takes for the data to be both compromised and available.

# Requirements on the integrity of the evidence

When LE breaks down your door and tackles you to the ground, you are probably in the middle of destroying your server and laptops with a hammer or something. When you are finally restrained and handcuffed, the CHFI comes in and begins to go through the stuff you tried to wreck. Often by the Order of Volatility as mentioned below. 

But CHFI has standards and a code to abide by. But the main thing that they wished they had more of, above anything else, is TIME. 

Time to BUILD that case against you. And the harder you make it for them to make good use of that TIME, for example, by having all of your traffic and data obfuscated to appear as something unrelated to hacking, or following a daily procedure of evidence destruction, then the faster they need to work to find viable evidence. Before TIME (to your court hearing), RUNS OUT. 

So the goal is NOT to break your shit, but to COMPROMISE the data's integrity or RENDER UNUSABLE to the investigator. 

It's impossible to wipe the disk cleanly with zeroes with a early-warning of at least 24 hours (for modern hard disks). But if we switched the data or added something that called into question to the judge of our actual motives, we stand a better chance at walking away free out of the courthouse.

Still, if possible, always overwrite your disks with zeroes when given the opportunity to. Like I said before, you need about 24 hours for every 2 TB of data you are trying to cleanly overwrite. 

Be aware that as soon as you are in handcuffs, the CHFI lady now has all the damn time she wants. It's important to abide by your own procedure much like the CHFI.

# The Order of Volatility

The Order of Volatility is simply defined as the hierarchy of how "volatile" (volatile to loss of...) data is in a..


Most Volatile

to 

Least Volatile

Pyramid.

When the CHFI goes over the crime scene, he or she is following the Order of Volatility to recover evidence based on how likely or critical it will be lost and become irrecoverable. Generally, hard disks are the least volatile, and cache and RAM are the most volatile (RAM will not persist through a reboot so it's important to perform a memory dump, but a neat trick is to freeze the physical memory with canned freon to look at the dump in cleartext).

Partially destroyed hard disks can be recovered by connecting jumper alligator clips to parts of the motor. Hence the futility of smashing your beloved pwn-box. It's generally, a better idea if you just ran a powerful rare-earth magnet up and down the hard disk enclosure.



# Leveraging our control of the flow of forensically viable information

# Not completed yet
