#!/bin/bash
grep -oP "Failed password.*from \K\S+" auth.log | sort -u | wc -l
