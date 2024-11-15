Task 0:

Testing Your Asset Tool: Navigating the Choppy Waters of Command Injection!
Insecure applications can be tricked into running harmful commands, giving attackers control of the system. This happens when user input isn’t checked properly. To prevent this, applications need to thoroughly examine all inputs and use secure coding techniques.

Challenge

We’re building our Asset Discovery tool and integrating some new features. Before we release it, we need thorough testing. Can you help us ensure it’s secure?

This challenge revolves around the Command Injection vulnerability. The ping input is vulnerable. Your mission begins with identifying and exploiting the command injection vulnerability in the ping functionality.

Target Application: Asset Discovery tool
Initial Endpoint: http://web0x09.hbtn/
Useful instructions:
1. Log into Asset Discovery tool.
2. ping is vulnerable.
3. We can try and give it an input (google.com for example).
4. Flag Location `/0-flag.txt

======

Task 1:

Time to beat our ping tool’s defenses! Let’s inject some fun and uncover secrets!
Welcome back to the next phase of your journey through the world of Command Injection vulnerabilities, set against the backdrop of our enhanced Asset Discovery tool.

Your mission now is to test the improved security measures and exploit the command injection vulnerability in the ping functionality.

Challenge

We’re building our Asset Discovery tool and integrating some new features. We’ve added a security layer, and we think it’s more secure now. Can you test it and ensure it’s safe?

This challenge focuses on Command Injection. The ping input is still vulnerable, but with some added security measures.

Target Application: Asset Discovery tool
Initial Endpoint: http://web0x09.hbtn/app2/
Useful instructions:
1. Log into Asset Discovery tool.
2. ping is vulnerable.
3. We can try and give it an input (google.com for example).
4. To exploit this vulnerability, we need to use Bypass space, Bypass command check.
5. Flag Location is `/etc/1-flag.txt

======

Task 2:

Hacking our ping tool? Let’s uncover secrets and flag victory!
Here’s another step in our cyber adventure! Let’s move forward and dive into the challenge ahead.

Despite our efforts, vulnerabilities may still lurk. Your mission? To test the tool’s defenses, exploit its weaknesses, and uncover hidden flags.

Challenge

This challenge involves a tool that pings given hosts. The goal is to exploit a command injection vulnerability in the user-supplied domain. However, the application has blacklisted many commands and special characters, including spaces and slashes. To bypass the filter, you’ll need to construct the path for the flag using the HOME environment variable.

Target Application: Asset Discovery tool
Initial Endpoint: http://web0x09.hbtn/app3/
Useful instructions:
1. Log into Asset Discovery tool.
2. ping is vulnerable.
3. We can try and give it an input (google.com for example).
4. To exploit this vulnerability, we need to use Bypass space, Bypass command check.
5. The flag is in /var/2-flag.txt
6. Path crafted with HOME bypasses filter.
7. Player supplied with source code.

======

Task 3:

Admins trust you about as much as they trust a cat with a fishbowl! Can you still fish out that flag?
After previous exploits, trust is scarce. Only trusted admins will receive scan results. Can you still find the flag?

Even with our best efforts, vulnerabilities linger. Your challenge? Probe the tool’s defenses, exploit its flaws, and unveil hidden flags.

Challenge

This challenge uses a tool to ping specified hosts, aiming to exploit a command injection vulnerability in the user-supplied domain. Since the application does not provide an output, you need to use the nslookup command to send the flag file’s content to Burp Collaborator.

Target Application: Asset Discovery tool
Initial Endpoint: http://web0x09.hbtn/app4/
Useful instructions:
1. Log into Asset Discovery tool.
2. ping is vulnerable.
3. We can try and give it an input (google.com for example).
4. Use the nslookup command 
5. Flag Location "/var/www/3-flag.txt"

======

Task 4:

Time to map out vulnerabilities with nmap! Can you sneak past our defenses and unearth those open
ports?

Welcome to the next level of your cybersecurity adventure! We’re taking our Asset Discovery tool up a notch by integrating nmap for open port checks. But have we secured it enough

Nmap Time! Ready for a New Challenge? 🕵️‍

This challenge focuses on exploiting a command injection vulnerability within the nmap input.

Target Application: Asset Discovery tool
Initial Endpoint: http://web0x09.hbtn/app5/
Useful instructions:
1. Log into Asset Discovery tool.
2. The nmap input is vulnerable.
3. We can try and give it an input (127.0.0.1:3000 for example).
4. Flag Location /bin/4-flag.txt
