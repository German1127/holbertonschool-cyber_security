0. Will arp be enough ?

Write a bash script that scan a subnetwork to discover live host using ARP scan.

You should use nmap.
Your code should tell nmap not to do a port scan after host discovery.
You should run your code as privileged user. root or sudoers.
Your script should accept a subnetwork as an arguments $1.
Depending on the scanned subnetwork, the output could change.
We can’t expect to learn about the Target MAC Address, unless we are in the the same subnetwork.

#!/bin/bash
sudo nmap -sn -PR $1


#!/bin/bash:
This line tells the operating system that the following script should be executed using the Bash shell. Bash is a very popular shell on Unix-like systems like Linux and macOS.

sudo:
This keyword grants the script superuser (root) privileges. This is necessary because the nmap tool often requires access to ports and networks that are restricted to normal users.

nmap:
Nmap is a widely used networking tool for discovering hosts and services on a network. It is like a network radar, capable of scanning ports, detecting operating systems and applications, and much more.

-sn:
This option tells nmap to perform a network scan without opening any connections. This is faster and less intrusive than a full port scan.

-PR:
This option tells nmap to send ICMP ECHO REQUEST (ping) and ARP REQUEST packets to discover hosts on the network.


$1:
$1 is the first argument passed to the script when it runs. In this case, it is expected to be an IP address or a range of IP addresses.

=======

1. Host, do you hear me ?
Write a bash script that scan a subnetwork to discover live host using ICMP Echo scan.

You should use nmap.
Your code should tell nmap not to do a port scan after host discovery.
You should run your code as privileged user. root or sudoers.
Your script should accept a subnetwork as an arguments $1.
Depending on the scanned subnetwork, the output could change.

#!/bin/bash
sudo nmap -sn -PE $1

-PE:
This option tells Nmap to send ICMP ECHO REQUEST (ping) packets and ARP packets to discover hosts on the network. ICMP packets are commonly used to verify connectivity between two devices on an IP network, while ARP packets are used to map IP addresses to MAC addresses on a local network.

======

2. Time always matter
Write a bash script that scan a subnetwork to discover live host using ICMP Timestamp scan.

You should use nmap.
Your code should tell nmap not to do a port scan after host discovery.
You should run your code as privileged user. root or sudoers.
Your script should accept a subnetwork as an arguments $1.
Depending on the scanned subnetwork, the output could change.

#!/bin/bash
sudo nmap -sn -PP $1

-PP:
This option tells Nmap to send ICMP ECHO REQUEST (ping) packets and TCP SYN packets (without establishing a full connection) to discover hosts on the network. ICMP packets are commonly used to verify connectivity between two devices on an IP network, while TCP SYN packets are used to determine if a port is open on a host.

======

3. Sometimes we need Masks !
Write a bash script that scan a subnetwork to discover live host using ICMP Address Mask scan.

You should use nmap.
Your code should tell nmap not to do a port scan after host discovery.
You should run your code as privileged user. root or sudoers.
Your script should accept a subnetwork as an arguments $1.
Depending on the scanned subnetwork, the output could change.

#!/bin/bash
sudo nmap -sn -PM $1


-PM:
This option tells Nmap to send ICMP ECHO REQUEST (ping) packets and TCP ACK packets (without establishing a full connection) to discover hosts on the network. ICMP packets are commonly used to verify connectivity between two devices on an IP network, while TCP ACK packets are used to determine whether a port is in listening state on a host.

======

4. SYN Scan me
mandatory
Score: 100.00% (Checks completed: 100.00%)


Write a bash script that scan a subnetwork to discover live host using TCP SYN Ping scan.

You should use nmap.
Your code should tell nmap not to do a port scan after host discovery.
Your code should scan for those ports22,80,443.
Your script should accept a subnetwork as an arguments $1.
Depending on the scanned subnetwork, the output could change.

#!/bin/bash
sudo nmap -sn -PS22,80,443 $1

-PS22,80,443:
This option tells Nmap to send TCP SYN packets to the specified ports (22, 80, and 443) to discover active hosts and determine if those ports are open. These ports are common for services such as SSH (22), HTTP (80), and HTTPS (443).

======

5. Are your privileged enough to scan me ?
Write a bash script that scan a subnetwork to discover live host using *TCP ACK Ping * scan.

You should use nmap.
Your code should tell nmap not to do a port scan after host discovery.
Your code should scan for those ports 22,80,443.
You should run your code as privileged user. root or sudoers.
Your script should accept a subnetwork as an arguments $1.

#!/bin/bash
sudo nmap -sn -PA22,80,443 $1

-PA22,80,443:
This option tells Nmap to send TCP ACK packets to the specified ports (22, 80, and 443) to discover active hosts and determine if those ports are in listening state. ACK packets are commonly used to check if a port is open and waiting for connections.

======

6. UDP is our last hope
Write a bash script that scan a subnetwork to discover live host using UDP Ping scan.

You should use nmap.
Your code should tell nmap not to do a port scan after host discovery.
Your code should scan for those ports 53,161,162.
You should run your code as privileged user. root or sudoers.
Your script should accept a subnetwork as an arguments $1.

#!/bin/bash
sudo nmap -sn -PU53,161,162 $1

-PU53,161,162:
This option tells Nmap to send UDP packets to the specified ports (53, 161, and 162) to discover active hosts and determine if those ports are in listening state. UDP packets are commonly used for protocols such as DNS (53), SNMP (161), and SNMP Trap (162).
