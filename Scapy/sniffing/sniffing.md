# 🧪 Basic Packet Sniffing using Scapy

## 📌 Overview

This project demonstrates **basic network packet sniffing** using Python and the Scapy library.  
It captures live network traffic and displays packet summaries to understand common network protocols.

> ⚠️ This project performs **passive monitoring only**. No packet modification or attacks are involved.

---

## 🛠️ Tools & Environment

- **Operating System**: Kali Linux  
- **Programming Language**: Python 3  
- **Library**: Scapy (v2.6.1)  
- **Network Interface**: eth0  
- **Execution Mode**: Root privileges (`sudo`)

---

## 🎯 Objective

- Capture live packets from the network
- Observe real-time traffic flow
- Identify common protocols:
  - ARP
  - DNS
  - DHCP
  - TCP / UDP
  - mDNS
  - IPv4 & IPv6 traffic

---

## 📜 Sniffing Script

```python
from scapy.all import sniff

sniff(
    prn=lambda p: p.summary(),
    store=False
)
```

![script](screenshots/sniffing_script.png)


## 🧪 Testing 

The following commands were used to generate network traffic

![Testing](screenshots/sniffing_testing.png)

## 📡 Output

The sniffing script was executed using:
``` bash
sudo python3 basic_sniffer.py
``` 

![Output](screenshots/so1.png)
![Output2](screenshots/so2.png)

## ⚠️ Issue Encountered & Resolution

### ❌ Problem: Missing Default Route

During the initial testing phase, internet connectivity was unavailable.  
This occurred because the system did **not have a default route configured**, which is required to forward traffic outside the local network.

Running the following command confirmed the issue:

```bash
ip route
```
### ✅ Resolution: Manually Adding Default Route

To resolve the issue, a default route was added manually using the gateway provided by the VirtualBox host-only network:

``` bash
sudo ip route add default via 192.168.56.2 dev eth0
```
After adding the default route, internet connectivity was restored and packet sniffing successfully captured external traffic such as DNS and TCP connections.


### 🧠 Learning Outcome

This issue highlighted the importance of proper network routing configuration before performing packet sniffing.
