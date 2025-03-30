#  0. File Hub 

Your initial objective entails identifying the vulnerable endpoint and securing the flag located at /etc/0-flag.txt.

- Target Machine: Cyber - WebSec 0x07
- Main Endpoint: http://web0x07.hbtn/task0/list_file
```
Useful instructions:
1. Try to upload a file.
2. Check page source for evey endpoint.
3. Investigate links and how they are processed, and what parameters are accepted.
4. Experiment with altering the path and file names and check the result.
```
---

#  1. Another filter won't help 

**Your Mission**

A critical file named 1-flag.txt is hidden somewhere within the system. You’ve discovered a vulnerable endpoint that should let you retrieve it, but the path to the file might not be exactly what you expect. A developer note hints at a small typo or oversight in the path something about extra slashes or a hidden directory that could help you sneak past the filter `..//.

- Target Machine: Cyber - WebSec 0x07
- Main Endpoint: http://web0x07.hbtn/task1/list_file

PS : a filter has been implemented to prevent unconventional paths.

**Hints & Instructions*

Useful instructions:

- 1. Understand the Endpoint
	- Analyze what payloads the endpoint accepts and how it processes file paths.

- 2. Bypass Filters
	- Explore different sequences of special characters or “unconventional” path notations to bypass simplistic checks.

- 3. Look for the Developer’s Mistake
	- Keep an eye out for any mismatch or extra characters (like more . or / than usual) in the path references.
	- That small detail might be the key to slipping past the filter.

- 4. Test Edge Cases
	- Combine special characters carefully, considering how the filter might accidentally allow access if it’s only expecting very specific patterns.

---

#  2. Not even this can be bypassed 

A critical flag is hidden deep within /etc/2-flag.txt. The system guarding it has implemented multiple layers of filtering and validation, making traditional techniques ineffective. However, every defense has its blind spot—your mission is deconstructing it.

Your task is to investigate, exploit, and secure the endpoint.

- Target Machine: Cyber - WebSec 0x07
- Main Endpoint: http://web0x07.hbtn/task2/list_file

Challenge yourself to bypass it while respecting security boundaries.
```
Useful instructions:
1. Test Boundaries: Experiment with different encoding and payload techniques to understand how inputs are processed.
2.  Think Outside the Box: Consider less conventional methods of bypassing security filters.
```
---

#  3. The Jinja template 

Your objective as usual is identifying the vulnerable endpoint and securing the flag located at /etc/3-flag.txt.

- Target Machine: Cyber - WebSec 0x07
- Main Endpoint: http://web0x07.hbtn/task3/list_file
```
Useful instructions:
1. Create a rapport.
2. Try multiple types of payloads in the rapport.
```
Hint : all the rapport are a jinja template

---

#  4. Poison the logs 

As usual the objective is to capture the flag however this time the flag would be set to a random path on the server. to get it you will need to at least have a decent shell access .

- Target Machine: Cyber - WebSec 0x07
- Main Endpoint: http://web0x07.hbtn/find_your_shell/
```
Useful instructions:
1. Investigate what files you have permission to access.
2. Check paths under root 
```

