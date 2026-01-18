# Advanced-Firewall-Lab-Trilayer

# 🔐 Advanced Firewall Lab

A layered firewall laboratory demonstrating **defense-in-depth** using
**iptables**, **pfSense**, and **Python (Scapy)** in a controlled environment.

---

## 📌 Project Overview

This project is designed to showcase how firewall controls operate at
different layers of a network by integrating multiple open-source technologies.

The lab combines:

- **iptables** for host-based firewalling and traffic filtering on Linux
- **pfSense** for network perimeter firewalling, routing, and policy enforcement
- **Python (Scapy)** for packet inspection, traffic generation, and rule validation

Together, these components simulate a real-world enterprise firewall
architecture commonly used in SOC and Blue Team environments.

---

## 🧱 Architecture Overview

[ Attacker / Client ]
     |
     v
[ pfSense Firewall ]
     |
     v
[ Linux Host (iptables) ]
    |
    v
[ Python + Scapy Analysis ]


---

## 🔍 Components

### 🔹 iptables (Host Layer)
- Inbound and outbound traffic filtering
- Port-based and protocol-based rules
- Logging and rule testing

### 🔹 pfSense (Network Layer)
- Perimeter firewall policies
- NAT and routing control
- Traffic segmentation and rule enforcement

### 🔹 Python + Scapy (Packet Layer)
- Packet capture and inspection
- Custom traffic generation
- Validation of firewall rules

---

## 🎯 Project Objectives

- Understand firewall behavior at multiple network layers
- Implement and test firewall rules in real scenarios
- Analyze allowed and blocked traffic
- Gain practical experience aligned with SOC and Blue Team roles

---

## 🧪 What This Lab Demonstrates

- Defense-in-depth security architecture
- Practical firewall rule implementation
- Network traffic analysis and validation
- Integration of open-source security tools

---
