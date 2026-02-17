                                                                                                             
from scapy.all import *

def analyze_packet(pkt):
    if TCP in pkt:
        print(f"TCP: {pkt[IP].src} -> {pkt[IP].dst}")
    elif ICMP in pkt:
        print(f"ICMP: {pkt[IP].src} -> {pkt[IP].dst}")

sniff(filter="ip", prn=analyze_packet, store=False)


