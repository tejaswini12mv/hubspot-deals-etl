# HubSpot Deals ETL Integration

## HubSpot API

- Endpoint: /crm/v3/objects/deals
- Authentication: Private App Access Token
- Query Parameters:
  - limit
  - after
  - properties
  - archived
- Rate Limits: As per HubSpot documentation
- Error Handling: HTTP status codes and error messages

## ETL Connection

1. Use the access token stored in `.env`
2. Extract deals using pagination
3. Map HubSpot properties to PostgreSQL columns
4. Store ETL metadata: extracted_at, scan_id
