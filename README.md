# 🕵️‍♀️ Pseudo Wireshark – A Custom Packet Sniffer for Network Forensics

This project is a lightweight, educational packet sniffer designed for use in a **Network Forensics** course. Built with **Python**, **Scapy**, and a **Flask web interface**, it enables students to observe live network traffic and analyze packets in real-time from their browser.

---

## 🛠 Features

- ✅ Real-time packet capture with Scapy
- ✅ Web-based interface using Flask
- ✅ Interface selector with IP info
- ✅ Start/Stop packet capture controls
- ✅ Live packet display with auto-refresh
- ✅ Capture up to 100 most recent packets

---

## 📦 Requirements

- Python 3.8+
- [Npcap](https://nmap.org/npcap/) installed (required for Windows packet capture)
- Scapy
- Flask

You can install dependencies using:

```bash
pip install -r requirements.txt
