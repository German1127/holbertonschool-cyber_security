#!/bin/bash
sudo nmap -sA -p 80,443,21,22,23 -v "$1"
