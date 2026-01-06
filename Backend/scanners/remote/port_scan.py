import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT",
    8000: "HTTP-DEV"
}

def scan_ports(target):
    results = []

    for port, service in COMMON_PORTS.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)

            if sock.connect_ex((target, port)) == 0:
                results.append({
                    "port": port,
                    "service": service,
                    "status": "open",
                    "risk": "low" if port in [80, 443] else "medium",
                    "recommendation": f"Restrict access to {service} if not required"
                })

            sock.close()
        except Exception:
            continue

    return results
