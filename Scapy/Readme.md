# Scapy Firewall Validation Module

This directory contains Scapy scripts used to:
- Capture live network traffic
- Modify packet headers
- Validate firewall rules implemented using iptables and pfSense

## Structure
- sniffing/: Packet capture and protocol identification
- packet_modification/: Demonstrates packet field manipulation
- firewall_testing/: Tests firewall enforcement using crafted packets

## Usage
All scripts must be run as root:
sudo python3 script_name.py
