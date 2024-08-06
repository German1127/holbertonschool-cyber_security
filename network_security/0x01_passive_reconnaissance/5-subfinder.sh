#!/bin/bash
sudo subfinder -d "$1" -silent | dnsx -a -resp | sed 's/\[//g; s/\]//g' | awk '{print $1 "," $2}' > "$1.txt"
