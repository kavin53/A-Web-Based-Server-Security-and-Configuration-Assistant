import ssl
import socket
from datetime import datetime

def scan_ssl(target):
    results = []

    if target.startswith("http"):
        target = target.replace("https://", "").replace("http://", "")

    try:
        context = ssl.create_default_context()
        with socket.create_connection((target, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()

               
                expires = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
                days_left = (expires - datetime.utcnow()).days

                results.append({
                    "check": "SSL Certificate",
                    "status": "valid",
                    "issuer": dict(x[0] for x in cert["issuer"]),
                    "expires_in_days": days_left,
                    "risk": "low" if days_left > 30 else "high",
                    "recommendation": "Renew certificate if near expiry"
                })

                
                results.append({
                    "check": "TLS Version",
                    "status": ssock.version(),
                    "risk": "low" if ssock.version() in ["TLSv1.2", "TLSv1.3"] else "high",
                    "recommendation": "Disable old TLS versions"
                })

        return results

    except Exception as e:
        return [{
            "check": "SSL",
            "status": "failed",
            "error": str(e),
            "risk": "high",
            "recommendation": "Enable HTTPS with valid SSL certificate"
        }]
