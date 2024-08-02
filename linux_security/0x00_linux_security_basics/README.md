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

