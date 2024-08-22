#!/bin/bash
sudo nmap -p -PS 22,80,443 $1
