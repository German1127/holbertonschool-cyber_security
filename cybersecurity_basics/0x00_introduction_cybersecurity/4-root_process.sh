#!/bin/bash
User=$1
ps -u $User -o user,pid,%cpu,%mem,vsz,rss,tty,stat,start,time,cmd | grep -v " 0 0" | grep -v "grep"
