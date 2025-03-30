![image](images/1.png)


#  0. Analyze iptables Rules 

Write a script to display all current iptables rules in a readable format, including line numbers.
```
$ sudo ./0-iptables.sh
Chain DOCKER-USER (1 references)
num   pkts bytes target     prot opt in     out     source               destination

1        0     0 RETURN     0    --  *      *       0.0.0.0/0            0.0.0.0/0 
```
---

#  1. Audit SSH Configuration 

Write a script to check for and report any non-standard SSH configuration settings in /etc/ssh/sshd_config.
```
$ sudo ./1-audit.sh
Include /etc/ssh/sshdconfig.d/*.conf
KbdInteractiveAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC*
Subsystem       sftp    /usr/lib/openssh/sftp-server
PasswordAuthentication yes
PermitRootLogin yes
AuthorizedKeysFile .ssh/authorized_keys
TCPKeepAlive yes
   
```
---

#  2. Harden Linux Server 

Write a script to list all world-writable directories and set their permissions to a more secure level.
```
$ sudo ./2-harden.sh
/home/user1
/home/user2
/home/user3
/var/www/html/uploads
```
---

#  3. Identify Common Vulnerabilities 

Write a script to check for unpatched common vulnerabilities using lynis audit tool.
```
$ sudo ./3-identify.sh
[ Lynis 3.0.9 ]
################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.
  2007-2021, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################
[+] Initializing program
------------------------------------
  ###################################################################
  #                                                                 #
  #   NON-PRIVILEGED SCAN MODE                                      #
  #                                                                 #
  ###################################################################
  NOTES:
  --------------
  * Some tests will be skipped (as they require root permissions)
  * Some tests might fail silently or give different results
  - Detecting OS...                                           [ DONE ]
  - Checking profiles...                                      [ DONE ]
  ---------------------------------------------------
```
---

#  4. Check for NFS Vulnerabilities 

Write a script to scan for NFS shares that are accessible by anyone on the network.
```
$ sudo ./4-nfs.sh 192.168.1.100
Export list for 192.168.1.100:
/data (everyone)
/home (10.0.0.2)
```
---

#  5. Audit SNMP Configuration 

Write a script to find SNMP configurations that allow public accessi.
```
$ sudo ./5-snmp.sh
com2sec public default public
rocommunity public
```
---

#  6. Examine SMTP Server Settings 

Write a script to check the SMTP server configuration for lack of STARTTLS or other security features. If STARTTLS not configured return STARTTLS not configured
```
$ sudo ./6-smtp.sh
smtpd_tls_security_level = may
```
---

#  7. Simulate DoS Attack on HTTP Server 

Write a script to simulate a basic Denial of Service attack on an HTTP server using hping3.
```
$ sudo ./7-dos.sh 192.168.1.100
HPING 192.168.1.100 (eth0 10.0.0.2): rand data
Using eth0, addr: 10.0.0.2, MTU: 1500
HPING 192.168.1.100 (eth0 10.0.0.2) with 1460 data bytes
```
---

#  8. Check for Weak SSL/TLS Ciphers 

Write a script to test an SSL/TLS server’s ciphers and report any weak ciphers using nmap.
```
$ sudo ./8-cipher.sh 192.168.1.100
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-11 15:00 UTC
Nmap scan report for some_random_ip
Host is up (0.042s latency).

PORT    STATE SERVICE
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 2.01 seconds

Host script results:
| ssl-enum-ciphers:
|   TLSv1.2:
|     ciphers:
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (ecdh_x25519) - A
|     compressors:
|       NULL
|     cipher preference: server
|_  least strength: A
```
---

#  9. Implement Basic Firewall Rules 

Write a script to set up basic iptables firewall rules that block all incoming traffic except SSH.
**Note**: For this specific task, wc -l file should print 3.
