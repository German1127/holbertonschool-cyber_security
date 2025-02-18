# 0. Flag File Privilege Escalation 
The goal of this challenge is to gain elevated privileges on the linux machine.

Make sure to enumerate properly the running processes, scheduled tasks, services, permissions and user management in order to find a weakness that can be exploited to gain root permission on the machine.

The flag is under:`/root/flag.txt`

## Hint:
Focus on user permissions and available sudo commands.

Leverage the `choom` command with sudo privileges to escalate permissions and gain access to restricted files.

## target machine for this task:
**cyber shell 0x02 linux privesc task1**

---

# 1. Privilege Escalation through Cron Job Misconfiguration
The goal of this challenge is to gain elevated privileges on the linux machine. Make sure to enumerate properly the running processes, scheduled tasks, services, permissions and user management in order to find a weakness that can be exploited to gain root permission on the machine. 

## Environment:
 - Target File:`/root/flag.txt`
 - Vulnerable Area: Misconfigured cron jobs or writable scripts executed by cron with root privileges.
 - Permissions: The script is writable by your user.
Once root privileges are obtained, access the flag file and read its contents.

## target machine for this task:
**cyber shell 0x02 inux privesc task2**

---

# 2. SUID Binaries and Privilege Escalation Challenge
You are a security analyst tasked with auditing a Linux system for potential privilege escalation vulnerabilities. During your assessment, you discover several SUID binaries that might be misconfigured.

Your mission is to identify these binaries and exploit any vulnerabilities to gain root access.

## Objectives:
 - Identify SUID Binaries.
 - Analyze Binary Behavior.
 - Exploit Vulnerabilities.
 - Access the Flag.

## Target Environment:
 - Target File:`/root/flag.txt`
 - SUID Binaries: Look for common binaries or any custom binaries present on the system.

## target machine for this task:
**cyber shell 0x02 linux privesc task3**


