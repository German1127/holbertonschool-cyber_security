![image](images/1.png)

#  0. SHA1 

Write a bash script that hashes a given password

- You should use SHA-1 algorithm
- Your script should accept a password as an arguments $1
- The resulting hash must be stored in 0_hash.txt
- Depending on the given password, the output could change
```
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 ./0-sha1.sh "Holberton"
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat 0_hash.txt
808f94d2847fb381839b4bbbd7cdf30804fd47ac
```
---

#  1. SHA256 

Write a bash script that hashes a given password

- You should use SHA-256 algorithm
- Your script should accept a password as an arguments $1
- The resulting hash must be stored in 1_hash.txt
Depending on the given password, the output could change
```
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 ./1-sha256.sh "Holberton"
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat 1_hash.txt
77c4925c01e8d9f79c8a6a61685c6b3182be10f2fa553de915f3733ee19c0204
```
---

#  2. MD5 

Write a bash script that hashes a given password

- You should use MD5 algorithm
- Your script should accept a password as an arguments $1
- The resulting hash must be stored in 2_hash.txt
Depending on the given password, the output could change
```
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 ./2-md5.sh "Holberton"
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat 2_hash.txt
f3b21c0205fba4fc7e6cb96ae6edc950
```
---

#  3. Secure Password Hash 

Encrypting passwords with OpenSSL: because even secret handshakes need a touch of pizzazz!

Write a bash scriptthat accepts a password as argument $1, combines it with a random 16-character value using OpenSSL, and generate SHA-512 hash of the new password using OpenSSL.

- The resulting hash must be stored in 3_hash.txt
Depending on the given password, the output could change
```
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 ./3-password_hash.sh "maroua@123"
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat 3_hash.txt
SHA512(stdin)= e6ec54449afad599a6e98cf37e9cd541e6d758ae30760080f1c7a2c6934e94edb5fa358e21633c6ed9cfced7dcf60cff7291ac96e2ac21f9df4429e137ae240f
```
---

#  4. Wordlist Mode 

In Wordlist Mode, we’ll provide John with a list of passwords, we will use the well-known RockYou wordlist

Write a bash scriptthat crack the password using John the Ripper based on the file hash.txt

- You should use john
- You should use John the Ripper’s Wordlist Mode to attempt password cracking
- Your script should accept hash.txt as an arguments $1
- You should find the hashed passwords
```
echo "<hashed_passwords>" > 4-password.txt
```
```
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat hash.txt
42f749ade7f9e195bf475f37a44cafcb
fc5e038d38a57032085441e7fe7010b0
18f1072de45420e57fd22ee5bd59df9e
┌──(maroua㉿HBTN-LAB)-[~/holbertonschool-cyber_security/cybersecurity_basics/0x03_cryptography_basics]
└─🏴./4-wordlist_john.sh hash.txt
Using default input encoding: UTF-8
Loaded 3 password hash (Raw-SHA256 [SHA256 256/256 AVX2 8x])
Warning: poor OpenMP scalability for this hash type, consider --fork=2
Will run 2 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
Almost done: Processing the remaining buffered candidate passwords, if any.
*******
*******
*******
3g 0:00:00:00 DONE (2023-08-29 16:20) 0g/s 0p/s 0c/s 0C/s
Session completed.
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat 4-password.txt
*******
*******
*******
```
---

#  5. Windows Authentication Cracking 

Let’s explore NThash or NTLM, a hash format used in modern Windows systems to secure user and service passwords.

Write a bash scriptthat crack the password using John the Ripper based on the file hash.txt.

- You should find the hashed password
- Your script should accept hash.txt as an arguments $1
```
echo "<hashed_passwords>" > 5-password.txt
```
Hints
- You need to set the format flag to nt
```
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat hash.txt
895F465356A0403458759A6B104B7242
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 ./5-windowsjohn.sh hash.txt
john --wordlist=rockyou --format=nt window.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
****            (?)

1g 0:00:00:00 DONE (2023-09-22 16:16) 50.00g/s 3312Kp/s 3312Kc/s 3312KC/s jonny123..gatasalvaje
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed.
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptography_basics]
└─🏴 cat 5-password.txt
****
```
---

#  6. John Cracking! 

Write a bash scriptthat crack the password using John the Ripper based on the file crack.txt.

- You should find the hashed password
- Your script should accept crack.txt as an arguments $1
```
echo "<hashedpasswords>" > 6-password.txt
```
```
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat crack.txt
aee408847d35e44e99430f0979c3357b85fe8dbb4535a494301198adbee85f27
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴./6-crackjohn.sh crack.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA256 [SHA256 256/256 AVX2 8x])
Warning: poor OpenMP scalability for this hash type, consider --fork=2
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
*******          (?)

1g 0:00:00:00 DONE (2023-09-21 14:23) 25.00g/s 819200p/s 819200c/s 819200C/s 
Use the "--show --format=Raw-SHA256" options to display all of the cracked pa
Session completed. 
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat 6-password.txt
*******
```
---

#  7. Hashcat Straight Attack! 

Write a bash scriptthat crack the password using hashcat based on the file hash.txt.

- You should find the hashed password
- Your script should accept hash.txt as an arguments $1
```
echo "<hashed_passwords>" > 7-password.txt
```
```
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat hash.txt
5f4dcc3b5aa765d61d8327deb882cf99
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴./7-crack_hashcat.sh hash.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 4.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 15.0.7, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: cpu-skylake-avx512-Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz, 1418/2900 MB (512 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache building /usr/share/wordlists/rockyou.txt: 33553434 bytes (2Dictionary cache building /usr/share/wordlists/rockyou.txt: 67106869 bytes (4Dictionary cache building /usr/share/wordlists/rockyou.txt: 100660302 bytes (Dictionary cache building /usr/share/wordlists/rockyou.txt: 134213744 bytes (Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 24 secs

f9f90eeaf400d228facde6bc48da5cfb:******

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: f9f90eeaf400d228facde6bc48da5cfb
Time.Started.....: Tue Sep 26 09:56:04 2023 (0 secs)
Time.Estimated...: Tue Sep 26 09:56:04 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    24737 H/s (0.10ms) @ Accel:256 Loops:1 Thr:1 Vec:16
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 1536/14344385 (0.01%)
Rejected.........: 0/1536 (0.00%)
Restore.Point....: 1024/14344385 (0.01%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: kucing -> mexico1

Started: Tue Sep 26 09:54:39 2023
Stopped: Tue Sep 26 09:56:05 2023
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat 7-password.txt
*******
```
---

#  8. Hashcat Combination! 

Write a bash scriptthat combine two wordlists using hashcat

- You should find the final wordlists after combination
- Your script should accept wordlist1.txt as an arguments $1
- Your script should accept wordlist2.txt as an arguments $2
```
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat wordlist1.txt 
pass
123
hello
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat wordlist2.txt 
word
world
000
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 ./8-combination_hashcat.sh wordlist1.txt wordlist2.txt 
password
passworld
pass000
123word
123world
123000
helloword
helloworld
hello000
```
---

#  9. Hashcat Combination Attack 

Write a bash scriptthat crack the password using hashcat based on the previous task

- You should use hashcat
- Your script should accept hash.txt as an arguments $1
- You should find the hashed password.
```
echo "<hashed_password>" > 9-password.txt
```
Hints
- You should use wordlist1.txt, wordlist2.txtafter combination
```
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat hash.txt
5ad8699d82cd039cab4ed739590969b9
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴./9-attack_hashcat.sh hash.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 4.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 15.0.7, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: cpu-skylake-avx512-Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz, 1418/2900 MB (512 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Dictionary cache hit:
* Filename..: wordlist1.txt
* Passwords.: 3
* Bytes.....: 15
* Keyspace..: 3

Dictionary cache hit:
* Filename..: wordlist2.txt
* Passwords.: 3
* Bytes.....: 15
* Keyspace..: 3

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache hit:
* Filename..: wordlist1.txt
* Passwords.: 3
* Bytes.....: 15
* Keyspace..: 9

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.           

5ad8699d82cd039cab4ed739590969b9:********                
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: 5ad8699d82cd039cab4ed739590969b9
Time.Started.....: Tue Sep 26 14:56:48 2023 (0 secs)
Time.Estimated...: Tue Sep 26 14:56:48 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (wordlist1.txt), Left Side
Guess.Mod........: File (wordlist2.txt), Right Side
Speed.#1.........:    21940 H/s (0.01ms) @ Accel:256 Loops:3 Thr:1 Vec:16
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 9/9 (100.00%)
Rejected.........: 0/9 (0.00%)
Restore.Point....: 0/3 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-3 Iteration:0-3
Candidate.Engine.: Device Generator
Candidates.#1....: password -> ********

Started: Tue Sep 26 14:56:46 2023
Stopped: Tue Sep 26 14:56:50 2023
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat 9-password.txt
********
```

