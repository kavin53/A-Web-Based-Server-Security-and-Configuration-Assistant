import requests

SECURITY_HEADERS = {
    "Content-Security-Policy": "Protects against XSS attacks",
    "X-Frame-Options": "Prevents clickjacking",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "Strict-Transport-Security": "Enforces HTTPS",
    "Referrer-Policy": "Controls referrer information",
    "Permissions-Policy": "Restricts browser features"
}

def scan_headers(target):
    results = []

    if not target.startswith("http"):
        target = "http://" + target

    try:
        response = requests.get(target, timeout=5)
        headers = response.headers

        for header, purpose in SECURITY_HEADERS.items():
            if header not in headers:
                results.append({
                    "header": header,
                    "status": "missing",
                    "risk": "medium",
                    "description": purpose,
                    "recommendation": f"Add {header} header"
                })

    except Exception as e:
        return [{
            "error": str(e),
            "risk": "high",
            "recommendation": "Target unreachable or invalid"
        }]

    return results
