# HubSpot Deals ETL Service

This project is an ETL (Extract, Transform, Load) service for HubSpot Deals data.  
It extracts deals from HubSpot CRM using the HubSpot Deals API v3, stores them in PostgreSQL, and provides endpoints to trigger scans and fetch results.

---

## Project Overview

- **Extract**: Connects to HubSpot API and fetches deals for configured tenants.
- **Transform**: Converts HubSpot property types to PostgreSQL-compatible types.
- **Load**: Stores deals into PostgreSQL with multi-tenant support and ETL metadata tracking.
- **API**: Exposes endpoints to start ETL scans and retrieve scan results.

---

## Project Structure

hubspot-deals-etl/
│
├── docs/ # API, Database, and Integration documentation
├── hubspot_etl/ # Main ETL service scripts
├── tests/ # Optional test scripts
├── requirements.txt # Python dependencies
├── run_etl.py # Main entry point for ETL
└── .env.example # Environment variables template


---

## Setup Instructions

1. **Clone the repository**
bash
git clone https://github.com/tejaswini12mv/hubspot-deals-etl.git
cd hubspot-deals-etl
2. **Create Virtual environment**
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux / macOS
3. **Install dependencies**
  pip install -r requirements.txt
4. **Configure environment variables**
   cp .env.example .env
HUBSPOT_ACCESS_TOKEN=your_access_token_here
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hubspotdb
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_SCHEMA=hubspot
5. **Run ETL Service**
  python run_etl.py
ETL Metadata

extracted_at — Timestamp when data was fetched from HubSpot

scan_id — Unique UUID for each ETL batch

loaded_at — Timestamp when data was loaded into PostgreSQL
7. 
8. 
