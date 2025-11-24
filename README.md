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
```bash
git clone https://github.com/tejaswini12mv/hubspot-deals-etl.git
cd hubspot-deals-etl
