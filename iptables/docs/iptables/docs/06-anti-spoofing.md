# Anti-Spoofing Protection

## Purpose
Implements anti-spoofing controls to prevent attackers
from sending packets with forged or invalid source
addresses.

## What Is IP Spoofing
IP spoofing occurs when an attacker forges the source
IP address of packets to:
- Bypass access controls
- Obscure the true origin of traffic
- Exploit trust relationships

## Protections Implemented

### Invalid Packet Dropping
Packets marked as INVALID by connection tracking are
dropped immediately to reduce malformed or suspicious
traffic.

### Loopback Address Protection
Packets claiming to originate from the loopback range
(127.0.0.0/8) are dropped unless they arrive on the
loopback interface.

### Private Address Filtering
Private (RFC1918) address ranges are blocked when
received on an external interface, preventing spoofed
internal addresses from entering the system.

## Security Benefits
- Reduces attack surface
- Blocks common spoofing techniques
- Improves firewall robustness

## Limitations
- Must be adapted for internal network deployments
- Interface-specific rules are recommended in production

## Execution Order
This script runs after all baseline filtering and
rate limiting rules.
