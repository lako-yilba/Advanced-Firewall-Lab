from scapy.all import *

TARGET = "192.168.56.1"

def test_http():
    pkt = IP(dst=TARGET)/TCP(dport=80, flags="S")
    resp = sr1(pkt, timeout=2, verbose=0)

    if resp and resp.haslayer(TCP):
        print("[PASS] HTTP allowed")
    else:
        print("[FAIL] HTTP blocked")

def test_spoof():
    pkt = IP(src="127.0.0.5", dst=TARGET)/TCP(dport=80, flags="S")
    resp = sr1(pkt, timeout=2, verbose=0)

    if not resp:
        print("[PASS] Spoofed packet dropped")
    else:
        print("[FAIL] Spoofed packet accepted")

if __name__ == "__main__":
    test_http()
    test_spoof()
