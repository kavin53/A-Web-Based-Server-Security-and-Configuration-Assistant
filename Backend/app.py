from flask import Flask, request, jsonify
from flask_cors import CORS
from scanners.remote.port_scan import scan_ports
from scanners.remote.headers_scan import scan_headers
from scanners.remote.ssl_scan import scan_ssl
from scanners.remote.dir_scan import scan_directories
from scanners.analyzer.risk_analyzer import analyze_risk
from scanners.analyzer.risk_engine import calculate_risk




app = Flask(__name__)
CORS(app)

@app.route("/run-scan", methods=["POST"])
def run_scan():
        data = request.json
        target = data.get("target")

        all_results = []

        port_scan_results = scan_ports(target)
        ssl_scan_results = scan_ssl(target)
        header_scan_results = scan_headers(target)

        all_results.extend(port_scan_results)
        all_results.extend(ssl_scan_results)
        all_results.extend(header_scan_results)            

        risk_summary = calculate_risk(all_results)

        return jsonify({
        "target": target,
        "results": all_results,
        "risk_summary": risk_summary
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
