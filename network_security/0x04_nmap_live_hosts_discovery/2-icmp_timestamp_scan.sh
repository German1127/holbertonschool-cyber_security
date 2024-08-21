#!/bin/bash
sudo nmap -sn --script icmp-timestamp $1
