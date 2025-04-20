# app.py
from flask import Flask, jsonify, render_template
from scapy_sniffer import captured_packets, start_sniffing
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/packets')
def get_packets():
    return jsonify(captured_packets[-50:])  # Return the last 50 packets

if __name__ == '__main__':
    # Start sniffing in a background thread
    sniffer_thread = Thread(target=start_sniffing, daemon=True)
    sniffer_thread.start()

    # Start the web server
    app.run(debug=True, port=5000)
