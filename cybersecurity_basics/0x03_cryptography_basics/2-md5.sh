#!/bin/bash
echo -n "$1" | md5sum | cut -d ' ' -f 1 | tr -d '\n' > 2_hash.txt

