# pfSense Firewall Installation (VirtualBox Lab)

## Objective
Set up pfSense CE as a firewall in a VirtualBox lab environment
to understand firewall deployment, interface assignment,
and network segmentation.

---

## Environment

- Host OS: Windows 11
- Hypervisor: VirtualBox
- pfSense Version: 2.8.1-RELEASE
- WAN: NAT
- LAN: Host-only Adapter

---

## Network Design

| Interface | Role | IP |
|---------|----|----|
| em0 | WAN | DHCP (NAT) |
| em1 | LAN | 192.168.56.2/24 |

---

## Installation Steps

1. Downloaded Netgate installer (`.iso.gz`)
2. Extracted `.iso` using 7-Zip
3. Created VirtualBox VM:
   - OS Type: BSD → FreeBSD (64-bit)
4. Attached installer ISO
5. Completed pfSense installation with:
   - Auto (UFS)
   - Default keymap
6. Rebooted and removed ISO

---

## Interface Assignment

- WAN → em0
- LAN → em1
- VLANs → Not configured

---

## LAN Configuration

- Static LAN IP: `192.168.56.2/24`
- DHCP enabled:
  - Start: `192.168.56.10`
  - End: `192.168.56.100`
- WebConfigurator: HTTPS

---

## Issues Faced & Fixes (Troubleshooting)

### Issue 1: Installer kept restarting
**Cause:** ISO was not removed after installation  
**Fix:** Removed ISO from VirtualBox storage

---

### Issue 2: Router login page appeared instead of pfSense
**Cause:** LAN was using `192.168.1.1` (conflict with home router)  
**Fix:** Changed pfSense LAN to `192.168.56.2`

---

### Issue 3: Web UI not reachable
**Cause:** IP conflict with VirtualBox Host-only adapter (`192.168.56.1`)  
**Fix:** Assigned pfSense LAN to `192.168.56.2`

---


## Final Result

- pfSense successfully installed
- Web UI accessible at:
https://192.168.56.2

- Firewall ready for rule configuration and NAT testing

---

## Key Learnings

- Importance of IP planning
- Host-only networking behavior in VirtualBox
- Difference between firewall IP and DHCP client range
- Real-world troubleshooting skills

---

## Next Steps

- Configure firewall rules
- Enable NAT policies
- Integrate pfSense into multi-firewall lab
