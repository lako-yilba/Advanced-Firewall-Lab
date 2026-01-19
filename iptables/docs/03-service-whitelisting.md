# Service Whitelisting

## Purpose
This component implements a service allow-list, permitting only
explicitly required inbound services while relying on a default-deny
policy for all other traffic.

## Why Service Whitelisting Is Important
Exposing unnecessary services increases the attack surface.
By allowing only required services, the firewall reduces the risk
of exploitation and unauthorized access.

## Services Allowed

### SSH (Port 22)
- Restricted to a trusted management IP address
- Used only for administrative access

### HTTP (Port 80)
- Allows inbound web traffic

### HTTPS (Port 443)
- Allows encrypted web traffic

## Design Considerations
- No explicit DROP rules are used
- All non-whitelisted traffic is implicitly blocked by the default policy
- New connections are explicitly allowed and tracked by conntrack

## Interaction With Other Firewall Components
- Relies on `02-stateful-filtering` to allow return traffic
- Works alongside rate limiting and anti-spoofing controls

## Verification
Expected behavior after applying these rules:
- Ports 22, 80, and 443 are accessible
- All other ports are blocked

Verification command:
```bash
nmap -p 1-1000 <firewall-ip>
