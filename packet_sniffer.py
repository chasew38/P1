from scapy.all import sniff
from datetime import datetime
import threading

captured_packets = []
stop_sniffing_event = threading.Event()

def packet_callback(packet):
    packet_info = {
        'time': datetime.now().strftime('%H:%M:%S'),
        'src': packet[0].src if hasattr(packet[0], 'src') else 'N/A',
        'dst': packet[0].dst if hasattr(packet[0], 'dst') else 'N/A',
        'summary': packet.summary()
    }
    captured_packets.append(packet_info)
    if len(captured_packets) > 100:
        captured_packets.pop(0)

def start_sniffing(interface):
    stop_sniffing_event.clear()
    sniff(iface=interface, prn=packet_callback, store=False,
          stop_filter=lambda x: stop_sniffing_event.is_set())

def stop_sniffing():
    stop_sniffing_event.set()

def get_packets():
    return captured_packets
