Task 0:

You might be familiar with the robust open-source network scanning tool Nmap, but have you heard about the even more potent Nmap Scripting Engine?

The Nmap Scripting Engine NSE is an advanced feature of the open-source network scanning tool Nmap . It automates network scanning and exploitation tasks, saving time and enhancing capabilities through scripting.
We have observed that many security professionals lack the ability to write NSE scripts for Nmap. This skill is relatively easy to learn, and by neglecting it, you are leaving a lot of value on the table. Let’s dive in and learn everything we need to become experts in the Nmap Scripting Engine today!

Write a bash script that runs the default NSE scripts using default to perform various analyses and gather necessary information related to the target.

Your script should accept a host as an arguments $1

======

Task 1:

Nmap’s vulners script is a powerful tool for identifying vulnerabilities on a target host. By leveraging a comprehensive database of known vulnerabilities, this script scans specified ports and services, providing detailed information about potential security issues.

Using the vulners script as part of regular security assessments can help organizations maintain robust defenses against emerging threats and ensure their systems remain secure.
Write a bash script that accepts a host as an argument $1.
Run the vulners script on the specified host, targeting ports 80 and 443.

======

Task 2:

The Nmap Scripting Engine NSE is a powerful feature of the Nmap network scanning tool, designed to automate various tasks, including vulnerability detection.
NSE scripts can identify weaknesses in network services, web applications, and configurations by leveraging a vast library of community-contributed scripts.

In this task, you’ll elevate your Nmap skills by using an NSE script to detect vulnerabilities in web applications.

Write a bash script that performs the following tasks:

Your script should accept a host as an arguments $1.
Use the http-vuln-cve2017-5638 NSE script to check for the Apache Struts 2 vulnerability.
Save the output to vuln_scan_results.txt for later analysis.

======

Task 3:

In this task, you’ll harness the power of the Nmap Scripting Engine NSE to perform a comprehensive security analysis of a target network

Write a bash script that performs the following tasks:

Your script should accept a host as an arguments $1.
Use multiple NSE scripts to perform a comprehensive security analysis, including:

http-vuln-cve2017-5638 for the Apache Struts 2 vulnerability.
ssl-enum-ciphers to enumerate supported SSL/TLS ciphers.
ftp-anon to check for anonymous FTP login.
Save the output to comprehensive_scan_results.txt for later analysis.

======

Task 4:

In this task, you’ll leverage the Nmap Scripting Engine (NSE) to automate the exploitation of vulnerabilities discovered during a network scan.

Write a bash script that performs the following tasks:

Your script should accept a host as an arguments $1
Use NSE scripts to detect vulnerabilities across various services:

Web Application Vulnerabilities: Your script should identify common vulnerabilities in web applications.
Database Vulnerabilities: Your script should detect vulnerabilities in MySQL .
Service Exploitation: Your script should check for exploitable conditions in FTP and SMTP.
Save the output to vulnerability_scan_results.txt for later analysis.

Note: Use * wildcard with NSE scripts for broader vulnerability coverage. exmple ftp-vuln*

======

Task 5:

When utilizing Nmap Scripting Engine (NSE), we harness a powerful capability within Nmap to automate and extend its network scanning functionalities.
NSE scripts enable us to perform a wide range of tasks beyond basic port scanning, including service version detection, vulnerability detection, enumeration of specific protocols like SMB and DNS, and even complex tasks like brute-force attacks and web application scanning.

Write a bash script that performs comprehensive network reconnaissance using Nmap with specific NSE scripts:

Your script should accept a host as an arguments $1
Your script should probe open ports to determine service/version information.
Your script should enable OS detection, version detection, script scanning, and traceroute.
Your script should execute multiple NSE scripts to detect vulnerabilities across various services:

Retrieve service banners from open ports.
Enumerate supported SSL/TLS ciphers..
Run default scripts default defined by Nmap for basic enumeration tasks.
Enumerate SMB (Server Message Block) domains.
Save the output to service_enumeration_results.txt for later analysis.
