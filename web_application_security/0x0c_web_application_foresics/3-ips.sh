#!/bin/bash
awk '/Failed password/ {print $(NF-3)}' auth.log | sort -u | wc -l
