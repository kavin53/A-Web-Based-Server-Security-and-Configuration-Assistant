import requests

COMMON_PATHS = [
    ".env",
    ".git/",
    "admin/",
    "backup/",
    "config/",
    "uploads/",
    "phpinfo.php",
    "test/",
    "old/"
]

def scan_directories(target):
    results = []

    if not target.startswith("http"):
        target = "http://" + target

    for path in COMMON_PATHS:
        url = f"{target.rstrip('/')}/{path}"
        try:
            r = requests.get(url, timeout=4, allow_redirects=False)

            if r.status_code in [200, 301, 302]:
                results.append({
                    "path": f"/{path}",
                    "status": "accessible",
                    "code": r.status_code,
                    "risk": "high",
                    "recommendation": "Restrict public access"
                })

        except Exception:
            continue

    if not results:
        return [{
            "status": "clean",
            "risk": "low",
            "recommendation": "No exposed directories detected"
        }]

    return results
