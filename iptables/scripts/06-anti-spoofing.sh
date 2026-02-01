#!/bin/bash
# Anti-Spoofing Protection Rules

# Drop INVALID packets
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

# Block loopback spoofing (127.0.0.0/8 not from lo)
iptables -A INPUT ! -i lo -s 127.0.0.0/8 -j DROP

# Block RFC1918 addresses on external interface (example: eth0)
iptables -A INPUT -i eth0 -s 10.0.0.0/8 -j DROP
iptables -A INPUT -i eth0 -s 172.16.0.0/12 -j DROP
iptables -A INPUT -i eth0 -s 192.168.0.0/16 -j DROP

# Optional: block link-local spoofing
iptables -A INPUT -i eth0 -s 169.254.0.0/16 -j DROP
