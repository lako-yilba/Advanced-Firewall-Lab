
# Firewall Configuration & Verification

This document provides a visual walkthrough of the iptables
firewall setup, rule verification, and live testing performed
as part of this project.

The screenshots are shown in the same order the firewall was
configured and tested.

---

The firewall is first reset and configured with a default
deny policy. INPUT and FORWARD chains are set to DROP, while
OUTPUT is allowed to maintain system usability.

![Baseline Firewall Policy](01.png)

---

Loopback traffic is explicitly allowed, followed by stateful
filtering rules that permit ESTABLISHED and RELATED traffic.
This ensures local services function correctly and return
traffic is not blocked.

![Loopback Rules](02.png)
![Stateful Filtering Rules](03.png)


---

Service whitelisting rules are applied to allow only required
services. SSH access is restricted to the local subnet, while
HTTP and HTTPS are selectively permitted.

![Service Whitelisting Rules](04.png)

---

Network Address Translation (NAT) masquerading is configured
to allow outbound traffic through the external interface.

![NAT Masquerading](05.png)

---

A successful SSH connection from an allowed source system
confirms that access control rules are functioning correctly.

![SSH Access Test](06.png)

---

An Nmap scan is performed from an external host to validate
that only intended ports are accessible and all other ports
are filtered.

![Nmap Scan Results](07.png)
