from scapy.all import sniff

sniff(
    prn=lambda p: p.summary(),
    store=False
)
