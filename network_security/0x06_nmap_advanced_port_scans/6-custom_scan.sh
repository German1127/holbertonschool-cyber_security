#!/bin/bash
sudo nmap --scanflags ALL -reason "$1" -p "$2" -oN custom_scan.txt >/dev/null 2>&1
