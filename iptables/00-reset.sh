## 00-reset.sh — Reset Existing Firewall Rules

### Purpose
This script flushes all existing iptables rules and deletes any
custom chains. It ensures the firewall starts from a clean and
predictable state before applying new rules.

### Why This Is Needed
Without resetting existing rules:
- Old or unknown rules may interfere with testing
- Debugging becomes difficult
- Firewall behavior becomes unpredictable

### What This Script Does
- Flushes rules from all tables (`filter`, `nat`, `mangle`, `raw`)
- Deletes all user-defined chains

### Script
```bash
iptables -F
iptables -X

iptables -t nat -F
iptables -t nat -X

iptables -t mangle -F
iptables -t mangle -X

iptables -t raw -F
iptables -t raw -X
```

### Command Explanation

- iptables -F
Flushes (removes) all rules from the default filter table.

- iptables -X
Deletes all user-defined chains in the filter table.

- iptables -t nat -F
Flushes all rules from the nat table.

- iptables -t nat -X
Deletes any custom chains in the nat table.

- iptables -t mangle -F
Flushes packet-altering rules from the mangle table.

- iptables -t mangle -X
Removes custom chains from the mangle table.

- iptables -t raw -F
Flushes rules from the raw table, which is processed
before connection tracking.

- iptables -t raw -X
Deletes any user-defined chains in the raw table
