#  0. Unlocking security, one exploit at a time! 

## Securing Your Shop’s Admin Dashboard: Charting a Course through Vulnerability Waters ⚓️!

**Shielding Shop Security..**

Welcome to the gateway of Server-Side Request Forgery SSRF, where you’ll embark on a journey through the digital landscape of vulnerabilities, set against the backdrop of our meticulously designed shop website. Your mission commences with probing the foundational element of SSRF vulnerabilities: uncovering potential gateways to unauthorized requests.

Before diving into the main challenge, let’s get you familiar with SSRF vulnerabilities. SSRF occurs when an attacker can make the server perform requests to arbitrary destinations on their behalf, often exploiting how URLs and parameters are handled. By learning about SSRF, we can start to uncover hidden security risks in systems. Let’s dive into the world of SSRF vulnerabilities and become experts at navigating the digital world.

Your mission is to test and secure our internal admin dashboard by identifying and exploiting potential SSRF vulnerabilities.

- Target Application: ShopAdmin
- Initial Endpoint: http://web0x08.hbtn/

```
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. The challenge is about the SSRF vulnerability in check reduction functionality.
3. You can click on one article and we see that we can do a check reduction.
4. Param artcileApi is vulnerable.
5. This App is Forwarded on Port 3000
```
---

#  1. Is our security a fortress or a sieve? Let's SSRF and find out! 

Following a thorough pentest, security measures were implemented to address known vulnerabilities. What about now, is it secure?

It’s time to put our defenses to the test and see if they can weather the storm of cyber threats. Your mission is to assess the effectiveness of these security enhancements and determine whether the system remains susceptible to SSRF attacks.

Even after adding mitigations, this stage remains focused on the SSRF vulnerability within the check reduction functionality. Let’s see if our enhancements are enough to secure the system

- Target Application: ShopAdmin
- Initial Endpoint: http://web0x08.hbtn/app2/
```
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. The challenge is about the SSRF vulnerability in check reduction functionality.
3. You can click on one article and we see that we can do a check reduction.
4. Bypass the filter by providing decimal representation of the localhost.
5. This App is Forwarded on Port 3001
```
---

#  2. Exploit SSRF to breach our security! 



We’ve been working on improving our security, and now it’s time to see how well it holds up. We’re especially focused on weaknesses that could allow unauthorized requests on the server SSRF vulnerabilities. By putting our system through rigorous testing, we’ll identify any areas that need more protection. Let’s find the chinks in our armor before anyone else does!

It’s time to pentest our added security by probing the SSRF vulnerability.

This stage also focuses on the SSRF vulnerability within the check reduction functionality. The articleApi parameter is vulnerable, and your goal is to exploit it to gain access to the internal admin dashboard.

- Target Application: ShopAdmin
- Initial Endpoint: http://web0x08.hbtn/app3/
```
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. The challenge is about the SSRF vulnerability in check reduction functionality.
3. You can click on one article and we see that we can do a check reduction.
4. Param artcileApi is vulnerable.
5.  This App is Forwarded on Port 3002
```
---

#  3. New security layers in town! Let's break 'em in and see if they hold up! 

Let’s see if our security makeover is more than just a fresh coat of paint! Time to poke some holes and find out!

This challenge focuses on the SSRF vulnerability within the check reduction functionality. Despite previous vulnerabilities, we’ve implemented new security measures. Now, it’s time to see if they’ve done the job.

Your mission is to test the new security layers: Attempt to exploit the SSRF vulnerability with the implementation of new security measures.

- Target Application: ShopAdmin
- Initial Endpoint: http://web0x08.hbtn/app4-1/

```
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. Navigate to Check Reduction Functionality: Explore the feature where the articleApi parameter is utilized.
3. There is New Feature To Navigate Product Now Trying Exploiting The Redirection in That  Feature  
4. Try Using The New Feature  as refer in your payload to  Exploit The Vulnerability 
5. Pay Attention To Other API Call to Backend Services & Port
6. This App is Forwarded on Port 3003 
```

