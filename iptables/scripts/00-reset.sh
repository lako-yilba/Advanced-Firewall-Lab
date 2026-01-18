#!/bin/bash
#
# WARNING:
# This script flushes ALL iptables rules and deletes ALL user-defined chains
# across filter, nat, mangle, and raw tables.
#
# Use ONLY in lab or controlled environments.
# Do NOT run on production systems or remote servers without console access.
#
# Purpose: Reset firewall state before applying new rules

# Flush all rules
iptables -F
iptables -t nat -F
iptables -t mangle -F
iptables -t raw -F

# Delete user-defined chains
iptables -X
iptables -t nat -X
iptables -t mangle -X
iptables -t raw -X
