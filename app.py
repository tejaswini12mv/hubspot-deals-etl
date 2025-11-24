from flask import Flask, request, jsonify
from services.extraction_service import ExtractionService
import os

app = Flask(__name__)
TOKEN = os.environ.get("HUBSPOT_ACCESS_TOKEN")  # make sure this env var is set
extraction_service = ExtractionService(TOKEN)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/deals/scan/start", methods=["POST"])
def start_scan():
    tenant_id = request.json.get("tenant_id")
    if not tenant_id:
        return jsonify({"error": "tenant_id required"}), 400
    result = extraction_service.start_scan(tenant_id, properties=[
        "dealname", "amount", "pipeline", "stage", "ownerid", "createdate", "closedate"
    ])
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5200)
