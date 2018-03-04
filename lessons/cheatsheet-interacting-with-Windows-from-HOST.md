# Copying files from Linux--->Windows using OpenSSH SCP (requires OpenSSH and Powershell Installed)


```
root@Lister-Unlimited-Hypervisor:~/Downloads# scp -r timesheet-bwsllc-012118.xlsx Chang@192.168.122.130:/C:/Users/Chang/Desktop
Chang@192.168.122.130's password: 
timesheet-bwsllc-012118.xlsx                                                                                    100%   99KB   1.0MB/s   00:00    
root@Lister-Unlimited-Hypervisor:~/Downloads# scp -r *.pdf Chang@192.168.122.130:/C:/Users/Chang/Desktop
Chang@192.168.122.130's password: 
Chapter 16 - Income Taxes(1).pdf                                                                                100%   69KB   3.1MB/s   00:00    
Chapter 19 - EPS(2).pdf                                                                                         100%   67KB   4.9MB/s   00:00    
exam2-f17.pdf                                                                                                   100% 5872KB   6.9MB/s   00:00    
exam2-s17.pdf                                                                                                   100% 5943KB   6.6MB/s   00:00    
ScheduleC Worksheet.pdf                                                                                         100%  519KB   9.4MB/s   00:00    
TAX INTERVIEW IN ENGLISH.pdf                                                                                    100%  119KB   6.4MB/s   00:00    
root@Lister-Unlimited-Hypervisor:~/Downloads# 
```
