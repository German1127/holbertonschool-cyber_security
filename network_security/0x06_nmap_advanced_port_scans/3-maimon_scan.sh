#!/bin/bash
sudo nmap -sA -p 80,443,21,22,23 -v "$1"
#Ports: http (80), https (443), ftp (21), ssh (22), telnet (23
