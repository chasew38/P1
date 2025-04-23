from flask import Flask, render_template, jsonify, request
from packet_sniffer import start_sniffing, get_packets
import threading
from scapy.all import get_if_list, get_if_addr

app = Flask(__name__)
sniffer_thread = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interfaces')
def interfaces():
    interfaces = []
    for iface in get_if_list():
        try:
            ip = get_if_addr(iface)
        except Exception:
            ip = "N/A"
        interfaces.append({
            "name": iface,       # used for sniffing
            "label": f"{iface} - {ip}"  # shown in dropdown
        })
    return jsonify(interfaces)


@app.route('/start_sniffing', methods=['POST'])
def start():
    global sniffer_thread
    interface = request.json.get('interface', 'eth0')
    if sniffer_thread is None or not sniffer_thread.is_alive():
        sniffer_thread = threading.Thread(target=start_sniffing, kwargs={'interface': interface})
        sniffer_thread.daemon = True
        sniffer_thread.start()
    return jsonify({'status': 'sniffing_started'})

@app.route('/packets')
def packets():
    return jsonify(get_packets())

if __name__ == '__main__':
    app.run(debug=True)
