#!/bin/bash
sha256sum -c "$2" > /dev/null 2>&1 && echo "OK" || echo "ERROR"
