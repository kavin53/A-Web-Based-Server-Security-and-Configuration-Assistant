from flask import Flask, request, jsonify
from flask_cors import CORS
from scanners.remote.port_scan import scan_ports
from scanners.remote.headers_scan import scan_headers
from scanners.remote.ssl_scan import scan_ssl
from scanners.remote.dir_scan import scan_directories
from scanners.analyzer.risk_analyzer import analyze_risk




app = Flask(__name__)
CORS(app)

@app.route("/run-scan", methods=["POST"])
def run_scan():
    data = request.json or {}
    scan_type = data.get("type")
    target = data.get("target")

    if not target:
        return jsonify({"error": "Target is required"}), 400

    if scan_type == "remote":
        results = scan_ports(target)

    elif scan_type == "headers":
        results = scan_headers(target)

    elif scan_type == "ssl":
        results = scan_ssl(target) 

    elif scan_type == "dir":
        results = scan_directories(target)

    else:
        return jsonify({"error": "Invalid scan type"}), 400

    risk_summary = analyze_risk(results)

    return jsonify({
        "target": target,
        "scan_type": scan_type,
        "results": results,
        "summary": risk_summary
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
