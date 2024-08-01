#!/bin/bash
ps -u "$1" | grep -vE "VSZ|RSS\s+0"
