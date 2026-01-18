# iptables Host-Based Firewall

## Overview
This directory contains a host-based firewall implemented using Linux iptables.
The firewall follows a default-deny security model and allows only explicitly
approved traffic.

This configuration is intended for learning and lab purposes.

---

## Design Approach
The firewall is implemented using modular scripts. Each script introduces
one security control, making the rules easier to understand, test, and maintain.

---

## Rule Execution Order
Rules must be applied in the following order:

1. `00-reset.sh` – Flush all existing firewall rules
2. `01-baseline-policy.sh` – Apply default deny policies
3. `02-stateful-filtering.sh` – Allow established and related connections
4. `03-service-whitelisting.sh` – Allow required services only
5. `04-nat-masquerade.sh` – Enable outbound NAT
6. `05-rate-limiting.sh` – Apply basic DoS protection
7. `06-anti-spoofing.sh` – Drop spoofed packets

---

## Security Concepts Implemented
- Default deny (zero trust)
- Stateful packet inspection
- Least privilege access
- Basic rate limiting
- Anti-spoofing controls

---

## Tables Used
- `filter` – Packet filtering
- `nat` – Network address translation

---

## Testing
Firewall behavior was validated using:
- Nmap port scanning
- Manual connectivity testing
- Packet inspection

---

## Screenshots
Screenshots showing the final firewall state and testing results are available
in the `screenshots/` directory.

---

## Limitations
- Firewall rules are not persistent across reboot
- Not production hardened
- No advanced IDS/IPS functionality
