<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Network Forensics Analyzer</title>
    <script>
        async function fetchPackets() {
            const res = await fetch('/api/packets');
            const data = await res.json();
            let table = '<tr><th>Time</th><th>Src</th><th>Dst</th><th>Proto</th><th>Len</th></tr>';
            for (let pkt of data) {
                table += `<tr>
                    <td>${pkt.timestamp}</td>
                    <td>${pkt.src}</td>
                    <td>${pkt.dst}</td>
                    <td>${pkt.proto}</td>
                    <td>${pkt.length}</td>
                </tr>`;
            }
            document.getElementById('packetTable').innerHTML = table;
        }

        setInterval(fetchPackets, 2000);
    </script>
</head>
<body>
    <h1>Live Packet Feed</h1>
    <table border="1" id="packetTable"></table>
</body>
</html>
