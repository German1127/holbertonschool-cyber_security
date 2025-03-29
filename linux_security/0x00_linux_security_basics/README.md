#  0. What secrets hold 

Write a bash script that shows you the last 5 logins session for users with their corresponding dates and times.

- You should run your code as privileged user. root or sudoers.

Depending on your machine, the output could change.

```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./0-login.sh
[sudo] password for maroua: 
root     tty1                          Thu Oct 12 10:08:24 2023   still logged in
root     ttyS0                         Thu Oct 12 10:08:23 2023   still logged in
reboot   system boot  6.5.0-kali1-clou Thu Oct 12 10:08:10 2023   still running
root     tty1                          Tue Oct 10 15:08:21 2023 - down                      (19:26)
root     ttyS0                         Tue Oct 10 15:08:21 2023 - down                      (19:26)

wtmp begins Mon Sep 25 16:29:08 2023 
```
---

#  1. Shows your Linux connections, not your social status! 

Write a bash script that display a list of network socket connections

- 1 You should run your code as privileged user root or sudoers.
- 2 You should Show all sockets, including listening and non-listening sockets.
- 3 You should Display numerical addresses (IP addresses and port numbers).
- 4 You should Limit the output to TCP sockets.
- 5 You should Display the process information associated with each socket.

**The task should use iproute2 version** 5.x

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./1-active-connections.sh
State   Recv-Q   Send-Q     Local Address:Port   Peer Address:Port   Process                                              
LISTEN  0        128                                          0.0.0.0:22                                           0.0.0.0:*                                                                          
LISTEN  0        100                                          0.0.0.0:5000                                         0.0.0.0:*                                                                          
LISTEN  0        5                                          127.0.0.1:5901                                         0.0.0.0:*                      users:(("Xtigervnc",pid=923,fd=9))                  
ESTAB   0        0                                          127.0.0.1:5901                                       127.0.0.1:36828                  users:(("Xtigervnc",pid=923,fd=38))                 
ESTAB   0        0                                          127.0.0.1:36828                                      127.0.0.1:5901                                                                       
ESTAB   0        0                                         6.19.156.8:5000                                      6.19.0.167:60812                                                                      
LISTEN  0        128                                             [::]:22                                              [::]:*                                                                          
LISTEN  0        5   
```
---

#  2. Firewall rules: Your network's first line of defense! 

Write a bash script that allow only incoming connections with the TCP protocol through port 80.

- You should run your code as privileged user. root or sudoers.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./2-incoming_connections.sh
[sudo] password for maroua:
Rules updated
Rules updated (v6)
```
---

#  3. Securing your network, one rule at a time! 

Write a bash script that list all the rules in the security table of the firewall.

- You should run your code as privileged user. root or sudoers.
- You should use the verbose mode.

Depending on your machine, the output could change. 
```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./3-firewall_rules.sh
[sudo] password for maroua: 
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         



Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         


Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
```
---

#  4. See what's talking, and who's listening! 

Write a bash script that list services, their current state, and their corresponding ports.

- 1 You should run your code as privileged user. root or sudoers.
- 2 You should show the PID and name of the program to which each socket belongs.
- 3 You should show numerical addresses (IP addresses and port numbers).
- 4 You should display listening sockets.
- 5 You should display TCP sockets.
- 6 You should display UDP sockets.

Depending on your machine, the output could change. 
```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./4-network_services.sh
[sudo] password for maroua: 
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name

tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      881/sshd: /usr/sbin 
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      913/python3

tcp        0      0 127.0.0.1:5901          0.0.0.0:*               LISTEN      923/Xtigervnc

tcp6       0      0 :::22                   :::*                    LISTEN      881/sshd: /usr/sbin 
tcp6       0      0 ::1:5901                :::*                    LISTEN      923/Xtigervnc

udp        0      0 0.0.0.0:68              0.0.0.0:*                           525/dhclient

udp6       0      0 fe80::85e:34ff:fea6:546 :::*                                622/dhclient
```
---

#  5. Where it talks, we all listen! 

Write a bash script that initiate a system audit for scanning the machine.

- You should run your code as privileged user. `root` or `sudoers`.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./5-audit_system.sh
[sudo] password for maroua: 

[ Lynis 3.0.8 ]

################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.

  2007-2021, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################


[+] Initializing program
------------------------------------
  - Detecting OS...                                           [ DONE ]
  - Checking profiles...                                      [ DONE ]

  ---------------------------------------------------
  Program version:           3.0.8
  Operating system:          Linux
  Operating system name:     Kali Linux
  Operating system version:  Rolling release
  Kernel version:            6.5.0
  Hardware platform:         x86_64
  Hostname:                  kali
  ---------------------------------------------------
  Profiles:                  /etc/lynis/default.prf
  Log file:                  /var/log/lynis.log
  Report file:               /var/log/lynis-report.dat
  Report version:            1.0
  Plugin directory:          /etc/lynis/plugins
  ---------------------------------------------------
  Auditor:                   [Not Specified]
  Language:                  en
  Test category:             all
  Test group:                all

...

================================================================================

  Lynis 3.0.8

  Auditing, system hardening, and compliance for UNIX-based systems
  (Linux, macOS, BSD, and others)

  2007-2021, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)

================================================================================

  [TIP]: Enhance Lynis audits by adding your settings to custom.prf (see /etc/lynis/default.prf for all settings)
```
---

#  6. Your eyes and ears on the network! 

Write a bash script that capture and analyze network traffic going through the system.

- You should run your code as privileged user. root or sudoers.
- You should limit the number of packets captured to 5

Depending on your machine, the output could change. 
```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./6-captureanalyze.sh
[sudo] password for maroua: 
tcpdump: data link type LINUXSLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
09:10:03.397281 eth0  In  IP ip-6-19-0-167.eu-central-1.compute.internal.36014 > ip-6-19-156-8.eu-central-1.compute.internal.5000: Flags [P.], seq 3466652703:3466652721, ack 3521647673, win 24559, options [nop,nop,TS val 17390194 ecr 4276499227], length 18
09:10:03.397474 lo    In  IP localhost.34870 > localhost.5901: Flags [P.], seq 4075666532:4075666544, ack 2019255620, win 24573, options [nop,nop,TS val 1065549505 ecr 1065549431], length 12
09:10:03.398937 eth0  In  IP ip-6-19-0-167.eu-central-1.compute.internal.36014 > ip-6-19-156-8.eu-central-1.compute.internal.5000: Flags [P.], seq 18:66, ack 1, win 24559, options [nop,nop,TS val 17390195 ecr 4276499227], length 48
09:10:03.398990 eth0  In  IP ip-6-19-0-167.eu-central-1.compute.internal.36014 > ip-6-19-156-8.eu-central-1.compute.internal.5000: Flags [P.], seq 66:82, ack 1, win 24559, options [nop,nop,TS val 17390195 ecr 4276499227], length 16
09:10:03.399029 eth0  Out IP ip-6-19-156-8.eu-central-1.compute.internal.5000 > ip-6-19-0-167.eu-central-1.compute.internal.36014: Flags [.], ack 82, win 455, options [nop,nop,TS val 4276499301 ecr 17390194], length 0
5 packets captured
27 packets received by filter
0 packets dropped by kernel
```
---

#  7. So fast, it'll make your router sweat! 

Write a bash script that scan a subnetwork to discover live host using scan.

- You should run your code as privileged user root or sudoers.
- Your script should accept a subnetwork as an arguments $1.

Depending on the scanned subnetwork, the output could change. 
```
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./7-scan.sh www.holbertonschool.com
[sudo] password for maroua:
[sudo] password for maroua: 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-19 15:46 UTC
Nmap scan report for www.holbertonschool.com (34.249.200.254)
Host is up (0.026s latency).
Other addresses for www.holbertonschool.com (not scanned): 52.17.119.105 63.35.51.142
rDNS record for 34.249.200.254: ec2-34-249-200-254.eu-west-1.compute.amazonaws.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https



Nmap done: 1 IP address (1 host up) scanned in 4.23 seconds
```

