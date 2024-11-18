Task 0:

Create a Bash script to identify the IP address responsible for the most requests in a log file, which is likely the source of a Denial of Service (DoS) attack.

Requirements:

Script Length: The script should be exactly two lines long.

Input: The script should accept the log file path as a command-line argument.

Functionality:

Extract IP addresses from the log file.

Count the occurrences of each IP address.

Identify and print the IP address with the highest number of requests.

Log File : logs.txt

TIP: see which Ip had the most requests

======

Task 1:

Create a Bash script to find the endpoint (URL) that received the most requests, indicating it was likely the target of the attack.

Requirements:

Script Length: The script should be less than 3 lines long.

the script should accept the log file path as a command-line argument.

Functionality:

Extract the requested URLs from the log file.

Count the occurrences of each endpoint and identify the most frequently requested one.

TIP: try to find where the most request have been sent

======

Task 2:

Create a Bash script to determine how many requests the attacker has sent, where the attacker is identified as the IP address with the highest number of requests.

Requirements:

The script should accept a log file as input.
It should:
Identify the IP address with the most requests (assumed to be the attacker).
Count the total number of requests made by that IP address.

======

Task 3:

Create a Bash script to find out which tool or library the attacker used by analyzing the User-Agent strings.

Requirements:

Script Length: The script should be less than 3 lines long.

Input: The script should accept the log file path and the attacker’s IP as arguments.

Functionality:

Filter the log for requests made by the attacker.

Extract and count the User-Agent strings to identify the tool/library used.

======

Task 4:

After navigating the complexities of web application incidents your final task is to compile and present your findings in a detailed incident report

This report should not only document the attacks and vulnerabilities you encountered during the project tasks but also highlight any additional security weaknesses identified through your investigation.
The goal is to create a comprehensive document that could be presented to an organization to help them understand the incident and implement the proposed remediation strategies.

TIP: what is the thing that will limit the usage of the server

Report Guidelines:
Your report should be structured and detailed, adhering to professional standards. Consider using a Google Doc for its collaborative features and accessibility. Here are key elements to include:

Introduction: Briefly outline the attack, its impact, and the purpose of the report.

Detailed Attack Analysis: Analyze the attack, detailing the source, targeted endpoints, request volume, and tools used.

Proposed Mitigation Strategy: Present an effective mitigation plan to prevent future attacks.

Justification for the Proposed Solution: Explain why the proposed solution is the best option based on industry standards.

Steps for Implementation: Outline the necessary steps to implement the mitigation.

Post-Implementation Monitoring: Specify the tools and methods for ongoing monitoring post-implementation.

Conclusion: Summarize the report, emphasizing the importance of the solution and future security.

Submission Instructions:
Create your report in Google Docs, ensuring it is well-organized and follows the guidelines provided.
Make sure to anonymize any sensitive information.
Upon completion, adjust the sharing settings to ‘Anyone with the link can view.
Submit the link to your report as part of your project completion.
