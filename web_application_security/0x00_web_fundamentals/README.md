Task 1:
Write a bash script that exploit host header injection using curl.

Initial Endpoint : http://web0x00.hbtn/reset_password

Your script should accept the NEW HOST as ARG 1 ("$1").

Your script should accept the TARGET URL as ARG 2 ("$2").

Your script should accept the FORM DATA as ARG 3 ("$3").

R:
#!/bin/bash
curl -s -X POST -H "Host: $1" -d "$3" "$2"


curl:
It is the tool that is being used to make the HTTP request.

-s:
This flag means "silent". Makes curl not display the progress bar or error messages, only the command output.


-X POST:
This flag indicates the HTTP method that will be used, in this case, POST. POST is commonly used to send data to the server.

-H "Host: $1":
This flag specifies an HTTP header. Here, the Host header is defined with the value of the first argument $1. HTTP headers are used to pass additional information with the request.


-d "$3":
This flag is used to send data in the body of the HTTP request. Here, the body content is taken from the third argument $3.

"$2":
This is the second argument and represents the URL to which the POST request will be sent.

======
