#!/bin/bash
grep "Failed password" auth.log | awk '{print $(NF-4)}' | sort -u | wc -l
