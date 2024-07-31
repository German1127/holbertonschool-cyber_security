#!/bin/bash
echo "$2 $1" | sha256sum -c -> /dev/null 2>&1 && echo "ok" || echo "invalid"
