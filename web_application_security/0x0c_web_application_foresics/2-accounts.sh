#!/bin/bash
tail -n 1000 auth.log | grep -E "Failed password|Accepted password" | awk '/Failed password/ {failed[$9]++}/Accepted password/ {success[$9]++}
END {
    for (user in success) {
        if (failed[user] && success[user]) {
            print user
        }
    }
}'
