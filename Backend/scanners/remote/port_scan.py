import socket
from unittest import result

COMMON_PORTS = {
    21:"FTP",
    22:"SSH",
    23:"TELNET",
    25:"SMTP",
    53:"DNS",
    80:"HTTP",
    110:"POP3",
    143:"IMAP",
    443:"HTTPS",
    3306:"MYSQL",
    8080:"HTTP-ALT"
}

def scan_ports(target, timeout=1):
    results = []

    for port , service in COMMON_PORTS.items():
        try:
            sock =socket.socket(socket.AF_INT, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            results = sock.connect_ex((target,port))
            sock.close()

            if results == 0:
                risk ="high" if port in[21,23,3306] else "meadium"
                results.append({
                    "port":port,
                    "service":service,
                    "status":"open",
                    "risk":risk,
                    "recommendation":f"Restrict access to {service} if not required"
                })

        except Exception:
            continue
    return results