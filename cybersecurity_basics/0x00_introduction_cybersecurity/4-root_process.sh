#!/bin/bash
User=$1
ps aux | grep User | grep -v "VSZ" | grep -v "RSS"
