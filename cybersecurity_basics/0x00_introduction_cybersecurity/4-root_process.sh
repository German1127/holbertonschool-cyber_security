#!/bin/bash
User="$1"
ps aux | grep "$User" | grep -v "grep" | awk '$5 > 0 && $6 > 0 {print $0}'
