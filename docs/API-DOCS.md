# HubSpot Deals ETL API Documentation

Replace <host> and <port> with environment:
- Dev: localhost:5200
- Stage: <stage-host>:5201
- Prod: <prod-host>:5202

## Authentication

Header:
Authorization: Bearer <HUBSPOT_ACCESS_TOKEN>

## Endpoints

### 1. Start Deals ETL Scan
POST /deals/scan/start

**Request Body:**
```json
{
  "tenant_id": "string",
  "limit": 100,
  "properties": ["dealname", "amount", "pipeline", "stage", "ownerid", "createdate", "closedate"]
}
{
  "scan_id": "uuid",
  "status": "started",
  "message": "ETL scan initiated successfully"
}
{
  "scan_id": "uuid",
  "status": "completed",
  "total_records": 100,
  "deals": [
    {
      "deal_id": 12345,
      "deal_name": "Example Deal",
      "amount": 10000.00,
      "pipeline": "default",
      "stage": "closedwon",
      "owner_id": 67890,
      "created_at": "2025-11-01T10:00:00Z",
      "closed_at": "2025-11-15T12:00:00Z"
    }
  ]
}
