0. Did you install kali 

Write a bash script that display the distributor ID in a concise single-line output.
Your Script Should Have one Line and New Line Only:

#!/bin/bash
lsb_release -is

#!/bin/bash 
:This line is the shebang. Indicates that the script should be run with the bash shell

lsb_release 
:It is a command that provides information about the Linux distribution.

-is 
:They are options passed to the command

-i 
:Display the name of the distribution

-s
:Suppresses additional details and displays only the relevant information.

======

1. We always need strong Passwords

Create a Bash script that generates a strong random password:
Your script should be less than 3 lines long.
You should accept password length as an args.
You should use /dev/urandom
You should use [:alnum:] as character classes.
The output may vary for each execution

#!/bin/bash
tr -dc '[:alnum:]' </dev/urandom | head -c "$1"

tr -dc '[:alnum:]'
:This command uses tr, which is a tool to translate or remove characters

-d 
:Remove the specified characters.

-c
:Complements the specified character set (in this case, all alphanumeric characters).

'[:alnum:]'
:Represents all alphanumeric characters (letters and numbers).


</dev/urandom
:This redirects input from the /dev/urandom device, which generates random data.

|
:The pipe symbol connects the output of the previous command to the next one.

head -c "$1"
:Use the head command to display only the first "$1" characters of the generated random sequence

======

2. Verify the integrity of a file

Create a Bash script that validate the integrity of a file:
Your script should be less than 3 lines long.

#!/bin/bash
echo "$2 $1" | sha256sum -c -

echo (command)
:The echo command is used to print text to standard output (usually the console). In this case, the concatenation of the arguments passed to the script is being printed: "$2 $1".

|
:The symbol | (pipe) is used to redirect the output of the previous command to the input of the next command. In this case, the output of echo is passed as input to the sha256sum command.

sha256sum
:This command calculates the SHA-256 hash of the data it receives as input. In this case, you are receiving the string generated by the echo

-c tells sha256sum to check the hashes provided in the input. In this case, the entry is expected to contain a SHA-256 hash followed by a file name.

======

3. We need an SSH key pair!
Create a Bash script that generates an RSA SSH key pair.

Your key size should be 4096
You Should Use Open-ssh

#!/bin/bash
ssh-keygen -t rsa -b 4096 -f "$1" -N ""

ssh-keygen
:It is the command that creates the SSH keys.

-t rsa
:Indicates that the RSA algorithm should be used to generate the keys.

-b 4096
:Sets the bit size of the key (in this case, 4096 bits).


-f "$1"
:Defines the name of the file where the private key will be saved. The value of "$1" will be replaced by the first argument provided to the script when it is run.

-N ""
:Set a password (passphrase) for the key. In this case, it is left blank so as not to have a password.

======

4. Let's Monitor root activity
Create a Bash script that monitors all processes started by specified user.

Your script should accept user as 1st agrs.
Your script should use grep -v to to exclude processes with VSZ and RSS values of 0
You Should Use ps command

#!/bin/bash
ps aux | grep "$1" | grep -v "vsz" | grep -v "rss"

ps aux
:This command lists all the running processes on the system with detailed information. The parameters mean:

a
:Shows the processes of all users.

u
:Shows the processes with the user format.

x
:Includes processes that do not have a control terminal (background processes).


|
:It is a pipe operator used to pass the output of one command as input to the next command.

grep "$1"
:grep is a search tool that searches for a text pattern in input. Here, "$1" is a variable that represents the first argument passed to the script or command. grep "$1" will find all lines in the output of the ps aux command that contain the text specified by the first argument.


grep -v "vsz"
:The second grep filters out lines containing the word "vsz". The -v option indicates that grep should exclude lines that match the pattern, rather than include them.

grep -v "rss"
:Similar to the previous one, this grep excludes lines containing the word "rss".


