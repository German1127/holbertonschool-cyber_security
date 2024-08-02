#!/bin/bash
last -n 5 | grep -v "reboot" | awk '{print $1, $2, $3, $4, $5, $6, $7}'
