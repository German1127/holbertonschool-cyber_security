#!/bin/bash
sudo nmap --scanflags ALL -reason "$1" -p "$2" > custom_scan.txt
