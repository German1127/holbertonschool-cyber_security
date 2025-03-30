#  0. Attacker Service 

## Unmasking Attackers, Securing the Future!

![image](images/0.webp)

The objective of this project is to develop scripts that analyze logs from web application attacks. These logs contain crucial information that can help us understand the nature of the attacks, identify the attackers, and uncover the vulnerabilities exploited. By scrutinizing these logs, we can gather actionable intelligence to strengthen our web application’s security posture.

Which service did the attackers use to gain access to the system? Write a script that scan the logs and help you figure what service was used 
```
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./0-service.sh 
34806 pam_unix(sshd:auth):
  20339 Failed
  14478 Invalid
    214 Address
    200 pam_unix(sshd:session):
    169 reverse
    118 Accepted
     44 Did
     20 error:
     20 Server
     10 subsystem
      9 syslogin_perform_logout:
      7 Received
      5 PAM
      5 Jax
      2 Bad
      1 new
      1 changed
      1 change
      1 Kayn
      1 Exiting
```
---

#  1. Operation System 

What is the operating system version of the targeted system

File Concerned is dmseg 
```
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./1-operating.sh 
[    0.000000] Linux version 2.6.24-26-server (buildd@crested) (gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)) #1 SMP Tue Dec 1 18:26:43 UTC 2009 (Ubuntu 2.6.24-26.64-server)
```
---

#  2. Account Compromised 

What is the name of the compromised account
```
* Tips: 
* Analyse last 1000 line of logs 
* Check if the user had multiple unsuccessful break in and then success  this will be mostly compromised account 
* Check for Suspected Activity 
```
```
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./2-accounts.sh 
root
```
---

#  3. Sum Attack 

Consider each unique IP address as representing a different attacker. How many distinct attackers gained access to the system
```
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./3-ips.sh 
18
```
---

#  4. Mitigation Firewalls 

How many rules have been added to the firewall
- Check the auth.log file for entries related to adding firewall rules.
```
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./4-firewall.sh
6
```
---

#  5. Users Accounts 

Multiple accounts were created on the target system. What are the users?

Example: **Aphelios,Debian-exim,Fido....**
```
┌──(imen㉿hbtn-lab)-[…/webapplicationsecurity/0x0cwebapplication_foresics]
└─$ ./5-users.sh
Aphelios,Debian-exim,Fido,Jax,Nidalee,Senna,dhg,messagebus,mysql,packet,sshd
```

