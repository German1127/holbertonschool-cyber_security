0. Are they any opened Port ?
In this project, tasks are arranged in a sequential manner to help you understand the basic principles of hacking and develop a logical approach to performing actions



Search for a door!
For this task we need you to:

Connect to the VPN server
Get Target Machine -> cyber_netsec_0x02
App
Endpoint: http://active.hbtn
Scan that Machine top ports using nmap.

======

1. Inspect the runner

Inspect the website!
For this task we need you to:

Edit /etc/hosts to point active.hbtn domain name to the Target IP.
sudo bash -c 'echo "<target_ip>    active.hbtn" >> /etc/hosts'

Inspect the found website.
Using Wappalyzer, check for webserver name and version

echo "<webservername> <webserverversion>" > 1-webserver.txt

======

2. Nothing defeat Manual inspection

Always check the SourceCode
For this challenge we need you to:

Browse active.hbtn
Search for the first flag.
echo "<FLAG_1>" > 100-flag.txt
Hints

Some Developer forgets comments in production.

App

Endpoint: http://active.hbtn

//press F12 in navigator//

======

3. Trypanophobia

Try to alter params, forms and queries..
For this task we need you to:

Search for vulnerable page.
echo "/<pathname>" > 2-injectable.txt
Don’t include params

Example: http://active.hbtn/orders/1511515

echo "/orders" > 2-injectable.txt
App
Endpoint: http://active.hbtn

======

4. SQLmap is an army \o/

Here we are at our first SQL Injection test

For this task we need you to:

Find the main Database name.
echo "<database_name>" > 3-database.txt
Check how many Tables it does contain
echo "<tables_count>" > 4-tables.txt
Hints

You need to use sqlmap
--dbs to fetch databases names
-D <database_name> --tables To fetch tables names

App

Endpoint: http://active.hbtn

sqlmap -u "http://active.hbtn/product/" active.hbtn --dump --dbs 

sqlmap: 
is an open source penetration testing tool that automates the detection and exploitation of SQL injection vulnerabilities in web applications

-u:
"http://active.hbtn/product/": Specifies the URL of the web page to be analyzed for SQL injections.

active.hbtn: 
Provides the name of the domain being analyzed.

--dump: 
Ask sqlmap to dump (extract) the contents of the database. This means that after identifying vulnerabilities, sqlmap will attempt to extract data from the database.

--dbs: 
Indicates that sqlmap should list the databases available on the target database system.

======

