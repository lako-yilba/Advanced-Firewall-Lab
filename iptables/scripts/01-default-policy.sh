#!/bin/bash
# Set default firewall policies

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
  echo "Run as root"
  exit 1
fi

# Default deny policy
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
