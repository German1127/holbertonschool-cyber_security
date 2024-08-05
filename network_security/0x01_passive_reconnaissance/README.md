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

