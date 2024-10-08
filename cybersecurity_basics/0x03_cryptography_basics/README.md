Task 0:

Write a bash script that hashes a given password

You should use SHA-1 algorithm
Your script should accept a password as an arguments $1
The resulting hash must be stored in 0_hash.txt
Depending on the given password, the output could change

======

Task 1:

Write a bash script that hashes a given password

You should use SHA-256 algorithm
Your script should accept a password as an arguments $1
The resulting hash must be stored in 1_hash.txt
Depending on the given password, the output could change

======

Task 2:

Write a bash script that hashes a given password

You should use MD5 algorithm
Your script should accept a password as an arguments $1
The resulting hash must be stored in 2_hash.txt
Depending on the given password, the output could change

======

Task 3:

Encrypting passwords with OpenSSL: because even secret handshakes need a touch of pizzazz!

Write a bash scriptthat accepts a password as argument $1, combines it with a random 16-character value using OpenSSL, and generate SHA-512 hash of the new password using OpenSSL.

The resulting hash must be stored in 3_hash.txt
Depending on the given password, the output could change

======

Task 4:

In Wordlist Mode, we’ll provide John with a list of passwords, we will use the well-known RockYou wordlist

Write a bash scriptthat crack the password using John the Ripper based on the file hash.txt

You should use john
You should use John the Ripper’s Wordlist Mode to attempt password cracking
Your script should accept hash.txt as an arguments $1
You should find the hashed passwords

======

Task 5:

Let’s explore NThash or NTLM, a hash format used in modern Windows systems to secure user and service passwords.

Write a bash scriptthat crack the password using John the Ripper based on the file hash.txt.

You should find the hashed password
Your script should accept hash.txt as an arguments $1
echo "<hashed_passwords>" > 5-password.txt

======

Task 6:

Write a bash scriptthat crack the password using John the Ripper based on the file crack.txt.

You should find the hashed password
Your script should accept crack.txt as an arguments $1
echo "<hashedpasswords>" > 6-password.txt

======

Task 7:
Write a bash scriptthat crack the password using hashcat based on the file hash.txt.

You should find the hashed password
Your script should accept hash.txt as an arguments $1
echo "<hashed_passwords>" > 7-password.txt

======

Task 8:

Write a bash scriptthat combine two wordlists using hashcat

You should find the final wordlists after combination
Your script should accept wordlist1.txt as an arguments $1
Your script should accept wordlist2.txt as an arguments $2

======

Task 9:

Write a bash scriptthat crack the password using hashcat based on the previous task

You should use hashcat
Your script should accept hash.txt as an arguments $1
You should find the hashed password.
echo "<hashed_password>" > 9-password.txt
