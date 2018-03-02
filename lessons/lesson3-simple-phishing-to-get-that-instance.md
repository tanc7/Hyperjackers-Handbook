If there is anything I know about the environment at UNLV. It's that...

You may think you are so smart falsely accusing me of being a hacker after your poor-assed student loans and all, but...


There is NO WAY that you could ever resist clicking on a #DicksUpForHarambe hashtag ;)

And it's going to download a stager payload (it was a bit.ly link after all, ahahaha!) that will install WannaCry32.exe without a trace, popup or dialogue on your screen.

# Phishing / Spearphishing. The easiest, most common and most successful attack vector.

I can show you how to phish or spearphish, without having to show you how to code at all! (But you definitely need to if you actually want to pull off a real hyperjacking)

There is a pretty neat, and up-to-date exploit kit on GitHub right now called Pupy. The pythonic reverse shell. One of the attack vectors happens to be one of the most commonly used against Windows victims in the last two years. It's called PowerShell. The situation has gotten so bad that Microsoft intentionally downgraded your ability to execute PowerShell files in later patches of Windows 10 like *.ps1 due to the onslaught of multi-stage payloads being sent through instant-messaging on facebook, your emails, and even text messages.

There are entire frameworks on post-exploitation with PowerShell, such as PowerShell Empire. Even Pupy's PowerShell payloads are partially based on PSE.

# Whats a stager?

Stagers are, my young naive student loan indebted friend, is actually a very old tactic designed to evade malware measures. The first stagers showed up back in the Windows 2000/Me days. Way before I even had a interest in hacking.

Instead of downloading a whole 120MB Windows PE32 (Portable executable format, any *.exe file in Windows), the stager downloads the entire malware kit in "stages", like the boosters of a space shuttle.

Generally there are a handful of components in a stager. For example...


1. JavaScript Downloader Stage 1: Sent to you by a phishing link like (Emgherd you won't believe  this shit https://you.tube://)
2. The JavaScript Downloader makes a Ajax Call to download Stage 2: a VBS (visual basic script) intermediary that bypasses your Windows 7 UAC (User Account Controls)
3. Which then downloads and runs by Elevated Powershell, a 'update.ps1' file Stage 3: That then compiles seemingly harmless individual Python *.py modules (At the time PowerShell commands apparently could run with full root privileges)
4. The command from PowerShell puts together update.exe using pyinstaller, that forces your Windows installation to compile update.exe using YOUR WINDOWS ENVIRONMENT.
5. Update.exe, stage 5: Executes itself via the PowerShell command, however Windows Defender catches it and kills it.
6. But uh oh! Lookout, now I, stage 6: Still reside inside of your computer's memory. Stage 6 contains commands to kill your puny Antivirus and avoid "touching the disk" until I know it';s just right. I need a way to elevate myself to SYSTEM (root for Windows) so I included a command to go off in 20 minutes from my execution. You know, something typical like "Explorer.exe crashed, would you like to run it?". It was a overlay meant to cover up the "Are you sure you want to run this as Administrator?" Prompt. But you are clearly too smart for me to fall for such a obvious trick.

So you clicked on it. As usual. Because you have too to do to double check on anything clearly. :D

Thanks man. Thanks for giving me full SYSTEM level root access into your Windows account not once, but TWICE. All because you thought that I was your best friend watching out for you because your sex tape with that one guy may have gotten leaked.


Well... now I do have your sex tape. In Pupy I also have the ability to send threatening dialogue boxes and popups to you remotely. If I manually uploaded a Metasploit payload and executed that (I have that power now), I can swap out the background wallpaper of your Apple TV with Tubgirl or Goatse. Right in the middle of your Greek Life Event.

And since you seem to have a lot of money and throw bitch-fits all the time, I am going to send segments of it to daddy until he pays me half a million. All in bitcoin payable to this address: asdasd12-0-o-909g=frhmm00i40-[2m]

Whats the matter. Don't know how to get Bitcoin? It's too hard?

My dear, if there is ANYTHING Americans are good at. It's making money. Rob a liquor store, hit the pole, or make another sex tape, I don't; care. 2 more minutes of the mistake of your life just got uploaded to xvideos.com and it just got 30,000 hits.

I know another person just like you, and she was very motivated to make me the money. Would you like to meet her? To help you make the money?

# SO how can YOU help motivate lazy American college kids to make you some money?
