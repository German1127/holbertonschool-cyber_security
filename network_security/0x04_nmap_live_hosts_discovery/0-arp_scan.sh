#!/bin/bash
^sudo nmap -sn -PR "$1" | grep "Nmap scan report for" | awk '{print $5}'

