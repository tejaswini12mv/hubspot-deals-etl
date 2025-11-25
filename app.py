from flask import Flask, request, jsonify
from flasgger import Swagger
from services.extraction_service import ExtractionService

app = Flask(__name__)

# Swagger configuration
swagger = Swagger(app)

# Your real HubSpot token here
TOKEN = "pat-na2-b7427c9e-14ce-4a56-aa38-57591f4dcb47"

# Initialize service
extraction_service = ExtractionService(TOKEN)


@app.route("/deals/scan/start", methods=["POST"])
def start_scan():
    """
    Start deal scan
    ---
    tags:
      - Deals
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            tenant_id:
              type: string
              example: tenant1
    responses:
      200:
        description: Scan started and list of deals returned
    """
    data = request.get_json()

    if "tenant_id" not in data:
        return jsonify({"error": "tenant_id is required"}), 400

    tenant_id = data["tenant_id"]
    result = extraction_service.start_scan(tenant_id)

    return jsonify(result)



@app.route("/deals/scan/<scan_id>/results", methods=["GET"])
def get_scan_results(scan_id):
    """
    Get scan results by scan_id
    ---
    tags:
      - Deals
    parameters:
      - name: scan_id
        in: path
        required: true
        type: string
        description: Scan ID received from /deals/scan/start
    responses:
      200:
        description: Results of the scan
    """
    result = extraction_service.get_scan_results(scan_id)
    return jsonify(result)



@app.route("/", methods=["GET"])
def home():
    return {
        "message": "HubSpot Deals ETL API running",
        "swagger": "/apidocs"
    }



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5200, debug=True)
