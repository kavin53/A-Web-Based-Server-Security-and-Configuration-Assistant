from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=['GET'])
def health():
    return jsonify({
        "status":"running",
        "project":"A Web-Based Server Security and Configuration Assistant"
    }),200

@app.route("/run-scan", methods=["POST"])
def run_scan():
    data = request.json

    scan_type = data.get("type")

    if scan_type not in ["remote","config","local"]:
        return jsonify({"error": "Invalid scan type"}),400

    return jsonify({
            "message": "Scan request received",
            "scan_type": scan_type,
            "next_step": "Scanner logic will be plugged here"
    }),200

if __name__ == "__main__" :
            app.run(debug=True)