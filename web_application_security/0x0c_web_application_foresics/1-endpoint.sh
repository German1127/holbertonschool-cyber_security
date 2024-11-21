#!/bin/bash
grep "Linux version" dmesg | sed 's/^/[    0.000000] /'
