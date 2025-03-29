#  0. Did you install kali ? 

Write a bash script that display the distributor ID in a concise single-line output.

- Your Script Should Have one Line and New Line Only

Do not use **awk**

```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_cybersecurity_basics]
└─$ ./0-release.sh
Kali
```
---

# 1. We always need strong Passwords 

Create a Bash script that generates a strong random password:

- Your script should be less than 3 lines long.
- You should accept password length as an args.
- You should use /dev/urandom
- You should use [:alnum:] as character classes.

The output may vary for each execution
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./1-gen_password.sh 20
MkPpprPyC3i6navUB3Lj
```
---

#  2. Verify the integrity of a file 

Create a Bash script that validate the integrity of a file:

- Your script should be less than 3 lines long.
- You can use echo in this task
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./2-sha256_validator.sh test_file e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855             
test_file: OK
```
---

#  3. We need an SSH key pair! 

Create a Bash script that generates an RSA SSH key pair.

- Your key size should be **4096**
- You Should Use **Open-ssh**
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./3-gen_key.sh new_key
Generating public/private rsa key pair.
Your identification has been saved in new_key
Your public key has been saved in new_key.pub
The key fingerprint is:
SHA256:aq73wv2/5u6k/qoGF83U3DZNsy5jg7Omv+zCSHkdbUM yosri@hbtn-lab
The key's randomart image is:
+---[RSA 4096]----+
|           o . +.|
|          . oE+ +|
|         +  o. o |
|        . o..+.  |
|        S..oo=.. |
|      .+.. .+ +  |
|     .+++  o.    |
|     o+.oo+o.    |
|    .o.+o=O&O.   |
+----[SHA256]-----+
                                                                                                                                                                                                                                            
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ls -l new_key*
-rw------- 1 yosri yosri 3381 Dec 19 18:50 new_key
-rw-r--r-- 1 yosri yosri  740 Dec 19 18:50 new_key.pub
```
---

#  4. Let's Monitor root activity 

Create a Bash script that monitors all processes started by specified user.

- Your script should accept user as 1st agrs.
- Your script should use grep -v to exclude processes with VSZ and RSS values of 0
- You Should Use ps command

The output may vary depending on your active processes
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./4-root_process.sh root
root           1  0.0  0.0  21172 12376 ?        Ss   07:38   0:01 /sbin/init splash
root         598  0.0  0.1  66380 19908 ?        Ss   07:39   0:00 /lib/systemd/systemd-journald
root         614  0.0  0.0 152264  1548 ?        Ssl  07:39   0:00 vmware-vmblock-fuse /run/vmblock-fuse -o rw,subtype=vmware-vmblock,default_permissions,allow_other,dev,suid
root         619  0.0  0.0  28688  8192 ?        Ss   07:39   0:00 /lib/systemd/systemd-udevd
root         768  0.0  0.0   8264  5304 ?        Ss   07:39   0:00 /usr/sbin/haveged --Foreground --verbose=1
root         779  0.0  0.0 315484 12708 ?        Ssl  07:39   0:30 /usr/bin/vmtoolsd
root        1005  0.0  0.0 311384  9268 ?        Ssl  07:39   0:00 /usr/libexec/accounts-daemon
root        1006  0.0  0.0   7032  2432 ?        Ss   07:39   0:00 /usr/sbin/cron -f
root        1014  0.0  0.0  17592  8320 ?        Ss   07:39   0:00 /lib/systemd/systemd-logind
root        1048  0.0  0.1 333664 20784 ?        Ssl  07:39   0:02 /usr/sbin/NetworkManager --no-daemon
root        1056  0.0  0.0 392124 11992 ?        Ssl  07:39   0:00 /usr/sbin/ModemManager
root        1119  0.0  0.0 382288  8900 ?        SLsl 07:39   0:00 /usr/sbin/lightdm
root        1121  0.0  0.2 2091040 44628 ?       Ssl  07:39   0:41 /usr/bin/containerd
root        1605  0.0  0.0 314176 12784 ?        Ssl  07:39   0:00 /usr/libexec/upowerd
root        1838  0.0  0.1 471588 18520 ?        Ssl  07:39   0:00 /usr/libexec/udisks2/udisksd
```

