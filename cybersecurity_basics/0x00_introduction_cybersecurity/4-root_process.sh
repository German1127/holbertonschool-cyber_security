#!/bin/bash
echo "$1" | ps -u "$1" | grep -vE "VSZ|RSS\s+0"
