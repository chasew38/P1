# scapy_sniffer.py
from scapy.all import sniff, IP, TCP, UDP
from threading import Thread
from datetime import datetime

# Shared list for storing captured packets
captured_packets = []

def packet_handler(pkt):
    if IP in pkt:
        protocol = 'TCP' if TCP in pkt else 'UDP' if UDP in pkt else 'Other'
        packet_info = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "src": pkt[IP].src,
            "dst": pkt[IP].dst,
            "proto": protocol,
            "length": len(pkt)
        }
        captured_packets.append(packet_info)

def start_sniffing():
    sniff(filter="ip", prn=packet_handler, store=0)
