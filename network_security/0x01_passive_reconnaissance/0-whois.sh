#!/bin/bash
sudo whois "$1" | awk /Registrant/ || /Admin/ || /Tech/ {print $1", " $2} > whois.csv
