0. What secrets hold

Write a bash script that show you the last 5 logins session for users with their corresponding dates.
You should run your code as privileged user. root or sudoers.

#!/bin/bash
sudo last -F -5

sudo
:Run the command with superuser privileges

last
:Command that displays a history of logins and events

-F
:Shows the exact login and logout time, including the logout date and time

-5
:Limits the output to the last 5 entries in the log. This is useful if you only want to see the most recent events

======

1. Shows your Linux connections, not your social status!
Write a bash script that display a list of network socket connections

1 You should run your code as privileged user. root or sudoers.
2 You should Show all sockets, including listening and non-listening sockets.
3 You should Display numerical addresses (IP addresses and port numbers).
4 You should Limit the output to TCP sockets.
5 You should Display the process information associated with each socket.

#!/bin/bash
sudo ss -t -a -p

sudo
:This command is used to run the following command with root privileges. This is necessary because some network-related operations require elevated permissions.

ss
:This is a Linux command used to investigate socket statistics, including active network connections. It is a modern replacement for the netstat command and is more efficient in terms of performance and resource usage.

-t
:This option is used to display only TCP (Transmission Control Protocol) connections. TCP connections are one of the most common types of network connections, used by protocols such as HTTP, FTP, and many others.

-a
:This option displays both active and listening connections.

-p
:This option displays the process (PID) and program name that is using each connection

======

2. Firewall rules: Your network's first line of defense!
Write a bash script that allow only incoming connections with the TCP protocol through port 80.
You should run your code as privileged user. root or sudoers

#!/bin/bash
sudo ufw allow 80/tcp

sudo
:This command is used to run the following command with root privileges. This is necessary because some network-related operations require elevated permissions.

ufw
:ufw stands for "Uncomplicated Firewall." It is a tool to manage firewall rules on Ubuntu-based systems and other Linux distributions.


allow
:It is an option of the ufw command that allows traffic through a specific port.

80/tcp
:Specifies the port and protocol to be allowed. Port 80 is used for HTTP traffic, and tcp indicates that it is the TCP communication protocol.

======

3. Securing your network, one rule at a time!
Write a bash script that list all the rules in the security table of the firewall.
You should run your code as privileged user. root or sudoers.
You should use the verbose mode.

#!/bin/bash
sudo iptables -L -v -n

sudo
:This command is used to run the following command with root privileges. This is necessary because some network-related operations require elevated permissions.

iptables
:It is a command line utility that allows you to configure the Linux system firewall. Manages packet filtering rules in the kernel.

-L
:Display the list of all rules in the iptables filter table.

-v
:Display detailed information about each rule, including packet and byte counters.


-n
:Display IP addresses and ports in numeric format instead of resolving host and service names. This speeds up the process and avoids potential delays in name resolution.

======

4. See what's talking, and who's listening!
Write a bash script that list services, their current state, and their corresponding ports.

1 You should run your code as privileged user. root or sudoers.
2 You should show the PID and name of the program to which each socket belongs.
3 You should show numerical addresses (IP addresses and port numbers).
4 You should display listening sockets.
5 You should display TCP sockets.
6 You should display UDP sockets.

#!/bin/bash
sudo netstat -tuln | ps aux

sudo
:This command is used to run the following command with root privileges. This is necessary because some network-related operations require elevated permissions.

sudo netstat -tuln
:Here the netstat command is used with sudo to run the command with superuser privileges. netstat is a tool that displays network connections, routing tables and interface statistics. The parameters used are:

-t
:Show TCP connections.

-u
:Show UDP connections.

-l
:Show only sockets that are listening.

-n
:Display addresses and port numbers in numeric format, rather than resolving to host or service names.

| ps aux
:The symbol | is a pipe that passes the output of the netstat command as input to the ps aux command. ps aux is a command that displays a list of all running processes on the system. The parameters used are:

a
:Shows the processes of all users.

u
:Shows the name of the user who executes the process.

x
:Shows processes that are not associated with a terminal.

======

5. Where it talks, we all listen!
Write a bash script that initiate a system audit for scanning the machine.
You should run your code as privileged user. `root` or `sudoers`.

///INSTAL LYNIS///

#!/bin/bash
sudo lynis audit system

sudo
:This command is used to run the following command with root privileges. This is necessary because some network-related operations require elevated permissions.


lynis audit system
:This is the command that runs the Lynis tool with the audit system parameter. Lynis is a security auditing tool for Unix-based operating systems, such as Linux. The audit system command performs a complete audit of the system, verifying configurations, possible vulnerabilities, and other security aspects

======

6. Your eyes and ears on the network!
Write a bash script that capture and analyze network traffic going through the system.
You should run your code as privileged user. root or sudoers.
You should limit the number of packets captured to 5

/// USE tcpdump -D FOR LIST///

#!/bin/bash
sudo tcpdump -i eth0 -c 5 -v

sudo
:This command is used to run the following command with root privileges. This is necessary because some network-related operations require elevated permissions.

tcpdump
:It is a command line tool for capturing and analyzing network packets on a system. Allows you to view network traffic passing through a specific interface.

-i eth0
:Especifica la interfaz de red a monitorear. En este caso, eth0 es el nombre de la interfaz de red. Esto podría variar dependiendo de la configuración del sistema; por ejemplo, puede ser eth1, wlan0, etc.


-c 5
:Defines the number of packets that must be captured before tcpdump stops. In this case, tcpdump will capture 5 packets and then stop automatically.

-v
:Es un nivel de verbose (detalle). -v incrementa la cantidad de información que tcpdump muestra sobre cada paquete. Puedes usar -vv o -vvv para más detalles.

======

7. So fast, it'll make your router sweat!
Write a bash script that scan a subnetwork to discover live host using scan.
You should run your code as privileged user root or sudoers.
Your script should accept a subnetwork as an arguments $1.

///INSTALL nmap///

#!/bin/bash
sudo nmap "$1"

sudo
:This command is used to run the following command with root privileges. This is necessary because some network-related operations require elevated permissions.


nmap
:is a networking tool used to scan and discover hosts and services on a network. It is commonly used for security audits and network mapping.

"$1": This represents the first argument passed to the script when it is executed
