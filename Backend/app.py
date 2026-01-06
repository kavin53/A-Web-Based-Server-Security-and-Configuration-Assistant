from flask import Flask, request, jsonify
from flask_cors import CORS
from scanners.remote.port_scan import scan_ports

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200

@app.route("/run-scan", methods=['POST'])
def run_scan():
    data = request.json or {}
    scan_type = data.get("type")

    if scan_type != "remote":
        return jsonify({"error": "Only remote scan implemented"}), 400
    
    target = data.get("target")
    if not target:
        return jsonify({"error": "Target is required"}), 400
    
    results = scan_ports(target)

    return jsonify({
        "target": target,
        "scan_type": "remote",
        "results": results
    }),200

if __name__ == "__main__":
    app.run(debug=True)
