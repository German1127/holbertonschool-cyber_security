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

#  3. Stealing Cookies from Managers is delicious ! 

Create a JavaScript payload that exploits Cross-Site Scripting (XSS) vulnerabilities within a ticketing system.

- Craft your payload using JavaScript.
	- It must be encapsulated within <script> tags.
	- Example format for your payload file: 
```
$ cat 3-xss_payload.txt
<script>// Your JavaScript code goes here</script>
```
- Your code should be as short as possible.
- You are not allowed to declare any variables within your payload.
- Your payload must utilize the fetch function to send the cookies of the ticket system’s visitor.
- The cookies should be included in the request’s pathname and sent to your designated web server.
		- Example: http://[your_ip]/.session=Tm90aGluZyBIZXJl]
- Initial Endpoint : http://web0x00.hbtn/login
---

#  4. Catch The FLAG #2 

Hint

- A Bot will load the ticket as a Support and response to it.
- Never forget that the XSS Payload will load on your side too !
- The Flag will be displayed on the <header> section after you sign in as a Support.

To Change your cookies, steps are simple:
```
Via FireFox:

-> Hit F12 (open dev tools)
-> Got to Storage (top menu)
-> Select Cookies
-> Change Value
```
---

#  5. Can we trust our Managers ? 

Here we are now, logged as a Support member. Now we can check tickets and reply to them!
What’s more interesting ? Yes! the Ticket ID which smell like SQLi \o/

- Write a text file containing the HTTP Request to exploit the potential SQL Injection in the ‘Ticket ID’ parameter.

Dev Tools -> Network, is the best path to go 
```
┌──(yosri㉿hbtn-lab)-[~/…/webapplicationsecurity/0x00webfundamentals]
└─$ sqlmap -r 5-ticket.txt
        ___
       H
 ___ [']__ ___ ___  {1.7.10#stable}
|--|.["]|.'|.|
||["]||_|,|__|
      ||V...       |_|   https://sqlmap.org
[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
[*] starting @ 09:31:09 /2023-11-13/
[09:31:09] [INFO] parsing HTTP request from '5-ticket.txt'
[09:31:10] [INFO] testing connection to the target URL
[09:31:10] [INFO] testing if the target URL content is stable
[09:31:10] [INFO] target URL content is stable
[09:31:10] [INFO] testing if GET parameter 'id' is dynamic
got a 302 redirect to 'http://web0x00.hbtn/support'. Do you want to follow? [Y/n]
```
- -Target Machine - Initial Endpoint : http://web0x00.hbtn/support
---

#  6. Catch The FLAG #3 

Hints

- You will need the file 5-ticket.txt from the previous task.
- For the admin credentials, they could be at Admins Table. SQLmap could --dump it for you.
- You could find the Admin login page at http://web0x00.hbtn/admin.
- The Flag will be displayed on the <header> section after you sign in as an Admin.
- Target Machine
- Initial Endpoint : http://web0x00.hbtn/admin

---

#  7. Why would an Admin have such a function ? 

Welcome to Admin Panel ! Things are getting dangerous here..
As we notice, there is a ping check function, which the admin use to up devices.

Write a payload that exploits poor input validation to achieve Remote Code Execution (RCE):

- Ensure there are no unnecessary spaces.
- Ensure your payload does exactly the following:
	- 1. Download the nc static binary using wget from https://github.com/yunchih/static-binaries/raw/master/nc.
	- 2. Grant execute permission to nc.
	- 3. Display the nc version using the -V option.
---

#  8. Catch The FLAG #4 
Hints

- Start a listner for reverse shell.
- ./nc to use netcat from the previous task.
- The Flag could be found at root‘s home directory

