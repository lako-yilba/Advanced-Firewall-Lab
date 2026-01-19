#!/bin/bash
# Allow loopback (localhost) traffic

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
  echo "Run as root"
  exit 1
fi

# Allow all traffic on loopback interface
iptables -A INPUT  -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
