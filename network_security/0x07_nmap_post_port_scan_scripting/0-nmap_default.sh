#!/bin/bash
sudo nmap -sC "$1" --script="$2"
