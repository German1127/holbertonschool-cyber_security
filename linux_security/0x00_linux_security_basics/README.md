0. What secrets hold

Write a bash script that show you the last 5 logins session for users with their corresponding dates.
You should run your code as privileged user. root or sudoers.

#!/bin/bash
sudo last -F -5

sudo
:Run the command with superuser privileges

last
:Command that displays a history of logins and events

-F
:Shows the exact login and logout time, including the logout date and time

-5
:Limits the output to the last 5 entries in the log. This is useful if you only want to see the most recent events

======

