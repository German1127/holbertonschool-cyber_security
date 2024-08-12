0. Who is it ?
Write a bash script that extract using whois scan in csv format:

Registrant Information
Admin Information
Tech Information
You are only allowed to use awk to format your output

#!/bin/bash
sudo whois "$1" | awk 'BEGIN{FS=": " ; OFS=","} /^Registrant/ || /^Admin/ || /^Tech/ {print $1", " $2}' > "$1.csv"

sudo whois "$1":
Runs the whois command with superuser (sudo) privileges for the argument passed to the script ("$1"), which is expected to be a domain. 
whois is a utility that queries the WHOIS database to obtain information about the owner of a domain.


| awk '...':
The output of the whois command is passed to awk, a powerful text processing language.


BEGIN{FS=": " ; OFS=","}:
BEGIN indicates that this section is executed before processing the input lines.
FS=": " sets the input field delimiter to : (colon followed by a space).
OFS="," sets the output field delimiter to a comma.

/^Registrant/ || /^Admin/ || /^Tech/:
This regular expression searches for lines that begin with "Registrant", "Admin", or "Tech". The operator || means "or", 
so lines that match any of these patterns will be selected.


{print $1", " $2}:
Prints the first and second fields of the matched line, separated by a comma. The first field is the contact type 
(e.g. "Registrant Name") and the second field is the corresponding value.

> "$1.csv":
La salida de awk se redirige a un archivo llamado como el dominio proporcionado ($1) con la extensión .csv

======

1. A record
Write a bash script that retrieve the A record of a specified domain using nslookup command:

#!/bin/bash
sudo nslookup -type=A "$1"

nslookup:
It is a command line tool used to query domain name servers and obtain DNS information.

-type=A: 
Specifies the type of DNS query to perform. Type A refers to address records, which correspond to IPv4 addresses.


"$1":
Refers to the first argument passed to the script. In this case, the user is expected to provide a domain name as an argument when running the script.

======

2. MX Record
Write a bash script that retrieve the MX record of a specified domain using nslookup command:

#!/bin/bash
sudo nslookup -query=MX "$1"


nslookup -query=MX:
This is the main command that performs the DNS query. nslookup is a tool for looking up DNS servers. The -query=MX option specifies that you want to query MX records, which indicate the email servers responsible for receiving mail for the specified domain.

======

3. Check the TXT
Write a bash script that retrieve the TXT record of a specified domain using nslookup command:

#!/bin/bash
sudo nslookup -query=TXT "$1"


nslookup -query=TXT "$1":
nslookup is a command line tool used to query domain name servers (DNS).
-query=TXT specifies that we want to query TXT records, which are a type of DNS record used to store arbitrary text.

======

4. Dig it all !
Write a bash script that retrieve All record of a specified domain using dig command:
Your output should contains answers only, noall

#!/bin/bash
sudo dig +noall +answer ANY "$1"

dig:
It is a command line tool used to perform DNS queries. It can be used to query records of different types, such as A, MX, TXT, etc.

+noall:
This is a dig option that suppresses all output except the response.

+answer:
Along with +noall, this option displays only the answers section of the DNS query.

ANY:
Specifies the type of DNS record to consult. ANY returns all records available for a domain.

======

5. Find the sub !
Write a bash script that fetch subdomains of given domain using subfinder command:

Show only subdomains in output
Write output in Host,IP format
File to write output to <domain>.txt

//INSTALL subfinder//

#!/bin/bash
sudo subfinder -silent -d "$1" -o $1.txt -nW -oI

subfinder:
It is a tool to discover subdomains.

-silent:
Run subfinder in silent mode, suppressing standard output.

-o $1.txt:
Save the output to a file with the domain name.

-nW:
Avoid recursive DNS queries, improving speed.

-oI:
Save only the identified subdomains in the output file.

======

7. Catch The flag - TXT

Here we come to our first CTF within this module. \o/

For this challenge we are expecting you to:

Target Domain passive.hbtn
Connect to the VPN server
Get a Target Machine
Use this <target IP> as a dns resolver within dig command

dig @<target IP> passive.hbtn
Hints

The flag is hidden within TXT record

======

8. Catch The flag - NS

For this challenge we are expecting you to:

Target Domain passive.hbtn
Connect to the VPN server
Get a cyber_netsec_0x01 Target Machine
Use this <target IP> as a dns resolver within dig command

dig @<target IP> passive.hbtn

The flag is hidden within TXT record

Try to search within nameserver domains

======

9. Catch the flag - MX

For this challenge we are expecting you to:

Target Domain passive.hbtn
Connect to the VPN server
Get a cyber_netsec_0x01 Target Machine
Use this <target IP> as a dns resolver within dig command
dig @<target IP> passive.hbtn

The flag is hidden within TXT record
Try to search within mail server domains
