#!/bin/bash
sudo nmap -sX -p 440-450 -v --open --reason -packet-trace "$1"
