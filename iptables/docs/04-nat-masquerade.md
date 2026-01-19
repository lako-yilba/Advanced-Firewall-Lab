# NAT Masquerading

## Purpose
Enables Network Address Translation (NAT) so that
internal hosts can access external networks using
the firewall's public IP address.

## What Masquerading Does
Masquerading rewrites the source IP address of outbound
packets to the IP address of the firewall interface.
Return traffic is automatically mapped back to the
originating internal host.

## Rules Applied
- Enable IPv4 forwarding
- Apply MASQUERADE rule in the POSTROUTING chain

## When This Is Needed
- Firewall acting as a gateway
- Internal hosts using private IP addresses
- Internet access through a single public interface

## Security Considerations
- NAT does not replace firewall filtering
- Only allowed traffic is forwarded
- Forwarding is still controlled by filter rules

## Execution Order
This script must run after baseline filtering rules
and before any port forwarding rules.
