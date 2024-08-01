#!/bin/bash
ps -u "$1" | grep -vE "VSZ|RSS|"0"
