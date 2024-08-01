#!/bin/bash
User=$1
ps aux | grep User | grep -v "vsz" | grep -v "rss"
