from flask import Flask, request, jsonify
from flask_cors import CORS

from scanners.remote.port_scan import scan_ports
from scanners.remote.ssl_scan import scan_ssl
from scanners.web.headers_scan import scan_headers
from scanners.web.dir_scan import scan_directories
from scanners.analyzer.risk_analyzer import calculate_risk

app = Flask(__name__)
CORS(app)

@app.route("/run-scan", methods=["POST"])
def run_scan():
    data = request.json
    scan_type = data.get("type")
    target = data.get("target")

    if not scan_type or not target:
        return jsonify({"error": "Missing scan type or target"}), 400

    results = []

    if scan_type == "port":
        results = scan_ports(target)

    elif scan_type == "ssl":
        results = scan_ssl(target)

    elif scan_type == "headers":
        results = scan_headers(target)

    elif scan_type == "dir":
        results = scan_directories(target)

    else:
        return jsonify({"error": "Invalid scan type"}), 400

    risk = calculate_risk(results)

    return jsonify({
        "scan_type": scan_type,
        "target": target,
        "results": results,
        "risk": risk
    })

if __name__ == "__main__":
    app.run(debug=True)
