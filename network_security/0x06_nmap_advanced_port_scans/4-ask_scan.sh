#!/bin/bash
sudo nmap -sA -reason "$1" -p "$2"
