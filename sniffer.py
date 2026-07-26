from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("\n===== Packet Captured =====")
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", packet[IP].proto)

# Capture 10 packets
sniff(prn=packet_callback, count=20)