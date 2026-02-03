from scapy.all import *

pkt = IP(dst="8.8.8.8") / TCP(dport=80, flags="PA") / Raw(load=b"Test payload")
send(pkt, verbose=False)
