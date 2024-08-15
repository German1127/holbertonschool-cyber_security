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

Add host:
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

5. Injections hurt :')
For this challenge we need you to:

Search for the second flag.
echo "<FLAG_2>" > 101-flag.txt

-D <database_name> --dump to dump the database.
Check for the Users table
Flag is exposed clearly in active.hbtn
App
Endpoint: http://active.hbtn

sudo sqlmap "http://active.hbtn/product/" -D active.hbtn --dump


sudo: 
Run the command with superuser privileges. This is useful if sqlmap requires elevated permissions to access certain resources or files.

sqlmap:
It is the tool used to detect and exploit SQL injection vulnerabilities.

"http://active.hbtn/product/": 
This is the URL of the website you are attacking. The goal here is to identify if the URL parameter is vulnerable to SQL injection.

-D active.hbtn: 
This argument indicates that you want to focus on the database called active.hbtn. Here you are specifying that sqlmap should interact with this particular database.

--dump: 
This parameter tells sqlmap to dump the entire contents of the selected database. This means that sqlmap will attempt to extract all tables and their data within the active.hbtn database.

======

6. My NAV doesn't include all my pages

Directory Enumeration
For this task we need you to:

Find the admin panel login page.
echo "/<pathname>" > 5-hidden_dir.txt
Hints

You need to use gobuster with dir option
-b 302 to ignore 302 status code.
-w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt for the wordlist
App
Endpoint: http://active.hbtn

//install gobuster//

sudo gobuster dir -u http://10.42.168.157 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -b 302 -o pruebagobuster.txt 

sudo: 
Run the command with superuser privileges.

gobuster dir: 
Indicates that Gobuster should perform a directory search.

-u http://10.42.168.157:
Specifies the URL of the target server.

-w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:
Defines the path of the wordlist file that Gobuster will use for searching. This file contains a list of common file and directory names.

-b 302:
Exclude HTTP responses with status code 302 (redirect).

-o testgobuster.txt: 
Save the search results to a file called testgobuster.txt.

======

7. It may look the same, but it’s not

For this challenge we need you to:

Search for the third flag.
echo "<FLAG_3>" > 102-flag.txt
Hints

Flag is exposed clearly in active.hbtn at Admin panel
App
Endpoint: http://active.hbtn

