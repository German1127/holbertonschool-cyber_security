#  0. Identify the Attack Source 

Create a Bash script to identify the IP address responsible for the most requests in a log file, which is likely the source of a Denial of Service (DoS) attack.

**Functionality:**

- Extract IP addresses from the log file.
- Count the occurrences of each IP address.
- Identify and print the IP address with the highest number of requests.
	- Log File : logs.txt
TIP: see which Ip had the most requests
```
┌──(oumaima㉿hbtn-lab)-[…/web_application_security/0x0b_web_application_fast_incident_response]
└─$  ./0-attack_ip.sh
**.***.**.**
```
---

#  1. Identify the Attacked Endpoint 

Create a Bash script to find the endpoint (URL) that received the most requests, indicating it was likely the target of the attack.

**Functionality:**

- Extract the requested URLs from the log file.
- Count the occurrences of each endpoint and identify the most frequently requested one.
TIP: try to find where the most request have been sent
```
┌──(oumaima㉿hbtn-lab)-[…/web_application_security/0x0b_web_application_fast_incident_response]
└─$  ./1-endpoint.sh 
/
```
---

#  2. Count the Number of Requests by the Attacker 

Create a Bash script to determine how many requests the attacker has sent, where the attacker is identified as the IP address with the highest number of requests.

**Requirements:**

- The script should accept a log file as input.
- It should:
	- 1. Identify the IP address with the most requests (assumed to be the attacker).
	- 2. Count the total number of requests made by that IP address.
```
┌──(oumaima㉿hbtn-lab)-[…/web_application_security/0x0b_web_application_fast_incident_response]
└─$  ./2-count_attack.sh
5000
```
---

#  3. Identify the Library Used by the Attacker 

Create a Bash script to find out which tool or library the attacker used by analyzing the User-Agent strings.

**Functionality:**

- Filter the log for requests made by the attacker.
- Extract and count the User-Agent strings to identify the tool/library used.
```
┌──(oumaima㉿hbtn-lab)-[…/web_application_security/0x0b_web_application_fast_incident_response]
└─$  ./3-library.sh
python-requests/2.31.0
```

