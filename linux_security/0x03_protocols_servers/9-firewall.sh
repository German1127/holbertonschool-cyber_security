#!/bin/bash
iptables -F; iptables -P INPUT DROP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
