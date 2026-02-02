# 🔍 Protocol Analyzer using Scapy

## 📌 Overview

This project implements a **basic protocol analyzer** using Python and the Scapy library.  
It captures live network traffic and classifies packets based on protocol type, specifically **TCP** and **ICMP**, displaying their source and destination IP addresses in real time.

> ⚠️ This project performs **passive packet analysis only**. No packet modification, spoofing, or attacks are performed.

---

## 🛠️ Tools & Environment

- **Operating System**: Kali Linux (VirtualBox)
- **Programming Language**: Python 3
- **Library**: Scapy
- **Network Interface**: eth0
- **Execution Mode**: Root privileges (`sudo`)
- **Firewall**: pfSense (ICMP blocked)

---

## 🎯 Objective

- Capture live IP traffic from the network
- Classify packets by protocol type
- Analyze **TCP** and **ICMP** traffic
- Display source and destination IP addresses
- Demonstrate protocol awareness at the network and transport layers

---

## 📜 Script

![Script](../screenshots/protocol_sniffer_script.png)


---

## 🧠 Script Explanation (High Level)

Capture-level filtering is applied using filter="ip" to ensure only IP packets are captured.

A callback function (analyze_packet) is executed for each packet.

Packets are classified using protocol layer checks:

TCP packets are identified using TCP in pkt

ICMP packets are identified using ICMP in pkt

Only essential metadata (source and destination IPs) is displayed to keep output clean and readable.

---

🧪 Testing

  ![Testing](../screenshots/protocol_sniffer_testing.png)

---
📡Output

![Output](../screenshots/po1.png)

---

## 🔐 Firewall Behavior Observed

During testing, ICMP echo replies were not received due to firewall rules configured in pfSense.

### Explanation

- TTL processing and packet transmission occurred correctly.
- ICMP response messages were filtered by the firewall.
- Packet capture remained unaffected.

This behavior is expected in secured environments and demonstrates the distinction between packet capture and packet response visibility.
---

## 🧠 Learning Outcome

Through this project, the following concepts were reinforced:

Packet sniffing using Scapy

Capture-level vs application-level filtering

TCP and ICMP protocol identification

Real-time packet analysis

Firewall impact on network visibility

Clean callback-based analyzer design
---
Note: HTTP analysis was not explicitly implemented as most modern web traffic is encrypted (HTTPS), making payload inspection ineffective without TLS decryption.
