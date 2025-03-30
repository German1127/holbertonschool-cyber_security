#  0. Who can add a new user in Linux! 

Write a bash script that generates a new user and sets a password for that specific user.

- Your script should accept a username as an arguments $1.
- Your script should accept a password as an arguments $2.
- File lines length = 3
- Not allowed to use printf
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./0-add_user.sh holberton H@ck$@f3Gu@rD!
[sudo] password for maroua:
New password: Retype new password: passwd: password updated successfully
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 tail -1 /etc/passwd
holberton:x:1005:1005::/home/holberton:/bin/sh
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo tail -1 /etc/shadow
[sudo] password for maroua:
holberton:$y$j9T$hX9xRbjAKGGXawAjjRbay.$byRISNEKNJeoUr5s8K4.QNDU5HgV2oocPJ6qYyBbHm0:19669:0:99999:7:::
```
---

#  1. Can we trust Groups ? 

Write a bash script that generates a new group, changes the ownership of the file to the new group and sets permissions for it.

- Your script should accept a group as an arguments $1.
- Your script should accept the file as an arguments $2.
- You should grant read and execute permissions to the newgroup on the file
- File lines length = 4
- Not allowed to use printf and echo
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./1-add_group.sh security example.txt
[sudo] password for maroua:
Adding group `security' (GID 1011) ...
Done.
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴cat /etc/group | grep "security"
security:x:1011:
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 ls -l example.txt
-rw-rwxr-- 1 maroua security 0 Nov  8 12:03 example.txt
```
---

#  2. Let's Add some fun ! 

Write a bash script that allows the user to execute the script without entering a password.

- Your script should accept the user as an arguments $1.
- File lines length = 2
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./2-sudo_nopass.sh maroua
[sudo] password for maroua:
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo cat /etc/sudoers
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        envreset
Defaults        mailbadpass
Defaults        securepath="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
Defaults        usepty
# This preserves proxy settings from user environments of root
# equivalent users (group sudo)
# Defaults:%sudo envkeep += "httpproxy httpsproxy ftpproxy allproxy noproxy"
# This allows running arbitrary commands, but so does ALL, and it means
# different sudoers have their choice of editor respected.
# Defaults:%sudo envkeep += "EDITOR"
# Completely harmless preservation of a user preference.
# Defaults:%sudo envkeep += "GREPCOLOR"
# While you shouldn't normally run git as root, you need to with etckeeper
# Defaults:%sudo envkeep += "GITAUTHOR* GITCOMMITTER*"
# Per-user preferences; root won't have sensible values for them.
# Defaults:%sudo envkeep += "EMAIL DEBEMAIL DEBFULLNAME"
# "sudo scp" or "sudo rsync" should be able to use your SSH agent.
# Defaults:%sudo envkeep += "SSHAGENTPID SSHAUTHSOCK"
# Ditto for GPG agent
# Defaults:%sudo envkeep += "GPGAGENT_INFO"
# Host alias specification
# User alias specification
# Cmnd alias specification
# User privilege specification
root    ALL=(ALL:ALL) ALL
# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
# See sudoers(5) for more information on "@include" directives:
@includedir /etc/sudoers.d
maroua ALL=(ALL) NOPASSWD: ALL
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
....
kali:x:1004:1004::/home/kali:/bin/sh
holberton:x:1005:1005::/home/holberton:/bin/sh
```
---

#  3. SUID hunting, Known Exploits! 

Write a bash script that searches for SUID vulnerabilities in a specified directory.

- Your script should accept the target directory as an arguments $1.
- File lines length = 2
NB: You should discard and not displayed on the terminal any error output.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./3-find_files.sh /usr/bin
[sudo] password for maroua:
-rwsr-xr-x 1 root root 76096 Aug 20 20:14 /usr/bin/su
-rwxr-sr-x 1 root shadow 31184 Mar 23  2023 /usr/bin/expiry
-rwxr-sr-x 1 root plocate 322960 Jul  4 16:24 /usr/bin/plocate
-rwsr-xr-x 1 root root 35128 Aug 20 20:14 /usr/bin/umount
-rwsr-xr-x 1 root root 30872 Aug  8 15:16 /usr/bin/pkexec
-rwsr-xr-x 1 root root 35128 Apr 18  2023 /usr/bin/fusermount3
-rwxr-sr-x 1 root ssh 493952 Sep  2 20:02 /usr/bin/ssh-agent
-rwsr-xr-x 1 root root 88496 Mar 23  2023 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 281912 Jul 19 22:31 /usr/bin/sudo
-rwsr-xr-x 1 root root 68248 Mar 23  2023 /usr/bin/passwd
-rwxr-sr-x 1 root shadow 80376 Mar 23  2023 /usr/bin/chage
-rwsr-xr-x 1 root root 63800 Aug 20 20:14 /usr/bin/mount
-rwsr-xr-x 1 root root 48896 Mar 23  2023 /usr/bin/newgrp
-rwsr-xr-x 1 root root 62672 Mar 23  2023 /usr/bin/chfn
-rwsr-xr-x 1 root root 52880 Mar 23  2023 /usr/bin/chsh
-rwxr-sr-x 1 root crontab 43648 Sep  3 10:30 /usr/bin/crontab
-rwxr-sr-x 1 root tty 39224 Aug 20 20:14 /usr/bin/wall
-rwsr-xr-x 1 root root 162752 Mar 23  2023 /usr/bin/ntfs-3g
-rwxr-sr-x 1 root tty 22848 Aug 20 20:14 /usr/bin/write
-rwxr-sr-x 1 root mail 23040 Feb  4  2021 /usr/bin/dotlockfile
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 wc -l 3-findfiles.sh
2 3-find_files.sh
```
---

#  4. Handle the SUID bit like a hot potato fun, but use it wisely! 

Write a bash script that lists all files with SUID set in a given directory

- Your script should accept the directory as an arguments $1.
- File lines length = 2
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./4-find_suid.sh Security
[sudo] password for maroua:
Security/holberton.sh
Security/flag.txt
Security/cybersecurity.txt
Security/100-flag.txt
```
---

#  5. Group hug your files with Setgid! 

Write a bash script that lists all files with SGID set in a given directory

- Your script should accept the directory as an arguments $1.
- File lines length = 2
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./5-find_sgid.sh Security
[sudo] password for maroua:
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo chmod g+s Security/*
[sudo] password for maroua:
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./5-find_sgid.sh Security
[sudo] password for maroua:
Security/cybersecurity.txt
Security/flag.txt
Security/holberton.sh
Security/100-flag.txt
```
---

#  6. Finding files with setuid or setgid! 

Write a bash script that Finds all files modified in the last 24 hours with SUID or SGID set and lists detailed information about those files .

- Your script should accept the directory as an arguments $1.
- You should use -mtime option.
- File lines length = 2
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴sudo ./6-check_files.sh Security
[sudo] password for maroua:
---S------ 1 maroua maroua 0 Jan  3 11:26 Security/100-flag.txt
---S------ 1 maroua maroua 0 Jan  3 11:26 Security/addgroup.sh
---S------ 1 maroua maroua 0 Jan  3 11:26 Security/sudofile.sh
---S------ 1 maroua maroua 0 Jan  3 11:26 Security/4-tcpsynping.sh
---S------ 1 maroua maroua 0 Jan  3 11:26 Security/5-tcpackping.sh
```
---

#  7. Others can read the files, but no writing privileges allowed—because files deserve their secrets too! 

Write a bash script that Changes permissions of all files in a directory to read-only for others without changing owner/group permissions.

- Your script should accept the directory as an arguments $1.
- File lines length = 2
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 ls -l Security/
total 6
-rwxrwxr-x 1 maroua maroua  33 Dec 19 11:00 0-arpscan.sh
-rw-rw-r-x 1 maroua maroua  33 Dec 19 11:00 101-flag.txt
-rwxrwxr-x 1 maroua maroua  33 Dec 19 11:00 1-icmpechoscan.sh
-rwxrwxr-x 1 maroua maroua  33 Dec 19 11:00 2-icmptimestampscan.sh
-rwxrwxr-x 1 maroua maroua  33 Dec 19 11:00 3-icmpaddressmaskscan.sh
-rwxrw-r-x 1 maroua maroua  43 Dec 19 11:00 6-udppingscan.sh
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴sudo ./7-file_read.sh Security/
[sudo] password for maroua:
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 ls -l Security/
total 6
-rwxrwxr-- 1 maroua maroua  33 Dec 19 11:00 0-arpscan.sh
-rw-rw-r-- 1 maroua maroua  33 Dec 19 11:00 101-flag.txt
-rwxrwxr-- 1 maroua maroua  33 Dec 19 11:00 1-icmpechoscan.sh
-rwxrwxr-- 1 maroua maroua  33 Dec 19 11:00 2-icmptimestampscan.sh
-rwxrwxr-- 1 maroua maroua  33 Dec 19 11:00 3-icmpaddressmaskscan.sh
-rwxrw-r-- 1 maroua maroua  43 Dec 19 11:00 6-udppingscan.sh
```
---

#  8. Changing file owners, one friendship at a time! 

Write a bash script that Changes permissions that changes the owner of files in a directory to user3, but only if the current owner is user2

- Your script should accept the directory as an arguments $1.
- File lines length = 2
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 ls -l Security/
total 6
-rwxrwxr-- 1 user2 maroua  33 Dec 19 11:00 0-arpscan.sh
-rw-rw-r-- 1 user2 maroua  33 Dec 19 11:00 101-flag.txt
-rwxrwxr-- 1 user2 maroua  33 Dec 19 11:00 1-icmpechoscan.sh
-rwxrwxr-- 1 user2 maroua  33 Dec 19 11:00 2-icmptimestampscan.sh
-rwxrwxr-- 1 user2 maroua  33 Dec 19 11:00 3-icmpaddressmaskscan.sh
-rwxrw-r-- 1 user2 maroua  43 Dec 19 11:00 6-udppingscan.sh
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./8-change_user.sh Security/
[sudo] password for maroua:
total 6
-rwxrwxr-- 1 user3 maroua  33 Dec 19 11:00 0-arpscan.sh
-rw-rw-r-- 1 user3 maroua  33 Dec 19 11:00 101-flag.txt
-rwxrwxr-- 1 user3 maroua  33 Dec 19 11:00 1-icmpechoscan.sh
-rwxrwxr-- 1 user3 maroua  33 Dec 19 11:00 2-icmptimestampscan.sh
-rwxrwxr-- 1 user3 maroua  33 Dec 19 11:00 3-icmpaddressmaskscan.sh
-rwxrw-r-- 1 user3 maroua  43 Dec 19 11:00 6-udppingscan.sh
```
---

#  9. Empty files got a promotion – now they're living large with full permissions! 

Write a bash script that finds all empty files in a directory and adds full permissions for everyone to these files.

- Your script should accept the directory as an arguments $1.
- File lines length = 2
Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 find Security/ -size 0 -exec ls -l {} \;
total 4
-rw-r--r-- 1 maroua maroua 0 Dec 20 09:40 ./cybersecurity.txt
-rw-r--r-- 1 maroua maroua 0 Jan  3 14:16 Security/flag.txt
-rw-r--r-- 1 maroua maroua 0 Jan  3 14:16 Security/example.txt
-rw-r--r-- 1 maroua maroua 0 Jan  3 14:16 Security/cybersecurity.txt
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴sudo ./9-empty_file.sh Security/
[sudo] password for maroua:
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 find Security/ -size 0 -exec ls -l {} \;
total 4
-rwxrwxrwx 1 maroua maroua 0 Jan  3 14:16 cybersecurity.txt
-rwxrwxrwx 1 maroua maroua 0 Jan  3 14:16 example.txt
-rwxrwxrwx 1 maroua maroua 0 Jan  3 14:16 flag.txt
-rwxrwxrwx 1 maroua maroua 0 Jan  3 14:16 holberton.sh
```


