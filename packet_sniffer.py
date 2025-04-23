from scapy.all import sniff
from datetime import datetime

captured_packets = []

def packet_callback(packet):
    packet_info = {
        'time': datetime.now().strftime('%H:%M:%S'),
        'src': packet[0].src if hasattr(packet[0], 'src') else 'N/A',
        'dst': packet[0].dst if hasattr(packet[0], 'dst') else 'N/A',
        'summary': packet.summary()
    }
    captured_packets.append(packet_info)
    if len(captured_packets) > 100:
        captured_packets.pop(0)  # keep it from growing forever

def start_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=False)

def get_packets():
    return captured_packets
