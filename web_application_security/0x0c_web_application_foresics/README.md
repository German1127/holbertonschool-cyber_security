Task 0:

Unmasking Attackers, Securing the Future!
The objective of this project is to develop scripts that analyze logs from web application attacks. These logs contain crucial information that can help us understand the nature of the attacks, identify the attackers, and uncover the vulnerabilities exploited. By scrutinizing these logs, we can gather actionable intelligence to strengthen our web application’s security posture.

Which service did the attackers use to gain access to the system? Write a script that scan the logs and help you figure what service was used

======

Task 1:

What is the operating system version of the targeted system

File Concerned is dmseg
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./1-operating.sh 
[    0.000000] Linux version 2.6.24-26-server (buildd@crested) (gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)) #1 SMP Tue Dec 1 18:26:43 UTC 2009 (Ubuntu 2.6.24-26.64-server)

======

Task 2:

What is the name of the compromised account

* Tips: 
* Analyse last 1000 line of logs 
* Check if the user had multiple unsuccessful break in and then success  this will be mostly compromised account 
* Check for Suspected Activity 
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./2-accounts.sh 
root

======

Task 3:

Consider each unique IP address as representing a different attacker. How many distinct attackers gained access to the system

┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./3-ips.sh 
18

======

Task 4:

How many rules have been added to the firewall

Check the auth.log file for entries related to adding firewall rules.
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./4-firewall.sh
6

======

Task 5:

Multiple accounts were created on the target system. What are the users?

Example: Aphelios,Debian-exim,Fido....

┌──(imen㉿hbtn-lab)-[…/webapplicationsecurity/0x0cwebapplication_foresics]
└─$ ./5-users.sh
Aphelios,Debian-exim,Fido,Jax,Nidalee,Senna,dhg,messagebus,mysql,packet,sshd

======

Task 6:

In cybersecurity, understanding and mitigating the risks associated with web application vulnerabilities is crucial. This report is the first entry in a comprehensive series on web application forensics, in which we explore the essential principles and strategies that can protect technology-enabled organizations against cyberthreats.

Instructions:

Introduction:
Analyzing web application logs allows for the identification of attacks and the development of protective strategies.
Draft an Incident Report:
Summarize the key findings and impacts of the recent security incident.
Develop an Implementation Plan:
Outline a step-by-step approach to apply the selected security measures.
Establish a Monitoring Protocol:
Create guidelines for ongoing evaluation of the security measures’ effectiveness.
