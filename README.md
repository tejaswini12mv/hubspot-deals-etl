# README.md
# HubSpot Deals ETL Service

## Overview
This project implements an ETL pipeline for HubSpot Deals data.  
It extracts deals via the HubSpot API, stores them in PostgreSQL, and supports multi-tenant data isolation.

## Features
- Extract deals from HubSpot CRM API v3
- Store data in PostgreSQL
- Track ETL metadata (extracted_at, scan_id)
- API endpoints to start scans and retrieve results
- Multi-tenant support

## Prerequisites
- Python 3.10+
- PostgreSQL
- pip

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/tejaswini12mv/hubspot-deals-etl.git
cd hubspot-deals-etl
```
2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```
3. Install dependencies:
```bash
pip install -r requirements.txt

```
4. Copy .env.example to .env and fill in your credentials:
```bash
cp .env.example .env
```
5. Run the ETL service (if Django/Flask implemented):
```bash
python manage.py runserver  # Django
# OR
python app.py  # Flask
```


HUBSPOT_ACCESS_TOKEN – Your HubSpot private app token

DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD – PostgreSQL connection

API Documentation:
See docs/API-DOCS.md for:
Authentication
Endpoints
Request/Response examples
Error codes

Database Schema:
See docs/DATABASE-DESIGN-DOCS.md for table structure, indexes, and multi-tenant design.

Integration Notes:
See docs/INTEGRATION-DOCS.md for HubSpot API details and ETL workflow.



