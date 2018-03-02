# Performing your first network-based Hyper-Jump to attack people in a wireless network


# Requirements

```
1. KVM Hypervisor
2. Debian or Ubuntu 9.3
3. Windows Server 2016
4. Windows 10 Education Edition (Same exact thing as Windows 10 Professional)*

*Avoid the Home Edition, they do not enable the proper privileges allowing you to fully manipulate the SMB protocol. Thats the shitty version thats preinstalled on all new laptops. If you are a college student, check the student bookstore if they let you get a copy for free.

```

# Overview of steps.

	1. Connect to your KVM virtual shell internally
	2. Start up Kali Linux VM inside of KVM with virtual shell
	3. From your HOST Hypervisor, create a networking route to your VM Kali Linux attacker instance
	4. Connect to the Wi-Fi Network
	5. From the HOST Hypervisor, "merge" the virtual network containing your VM instance with the real wireless network.
	6. Perform your first attack. "Nmap" a target from the perspective of your Kali Linux attacker VM.

