#!/bin/bash
top_ip=$(awk '{print $1}' logs.txt | sort | uniq -c | sort -nr | awk 'NR==1 {print $2}')
awk -v ip="$top_ip" '$1 == ip {print $0}' logs.txt | awk -F'"' '{print $6}' | sort -u
