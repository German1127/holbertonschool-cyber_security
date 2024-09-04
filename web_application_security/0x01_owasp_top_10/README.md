Task 0
Creating your own session IDs?, Make sure they’re as unpredictable as a plot twist in a mystery novel. If they’re too simple, it’s like leaving the keys in the ignition for hackers. Complexity and randomness are your locks and alarms.

For this task, tamper the hijack_session cookie to sneak into someone else’s session.

R: 
Press F12 on the page, go to the cookies section, capture several by opening the page several times until you find a relationship.

======

Task 1:
Create a Bash script that decode XOR WebSphere. Your Script should:
Accept the Hash args: $1.

======

Task 2:
For this task:

Turn back to the target machine cyber_websec_0x01,
Heads out to: A2 - Cryptographic Failures -> Encoding Failure.
Your goal is finding out the the login credentials in order to retreive the flag on sign in.

Login Page : http://[MACHINE-IP]/a2/crypto_encoding_failure/

Profile Page : /a2/crypto_encoding_failure/profile
hints:
Think about the headers of all Fetch/XHR made requests.
Use the previous task to decrypt the password.

R:
F12.
Inspect the "Network".
Search Fetch/XHR requests.
Authorization header. This header contains a token in bearer format, which appears to be an encoded JSON object.

you use the terminal in linux:
echo 'eyd1c2VybmFtZSc6ICd5b3NyaScsICdwYXNzd29yZF9oYXNoJzogJ0R6NThMeFZ2S0hJb0pTWWRPQkFxT0FZV05oTVFjaWdwS0E9PSd9' | base64 -d

Doing this returns the name and the encrypted pass, which is decoded with the script made in task 1 and gives the pass

======

