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


=======
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

## Django

SECRET_KEY=replace_me
DEBUG=True

Database (Postgres example)

DB_ENGINE=django.db.backends.postgresql
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=changeme
DB_HOST=127.0.0.1
DB_PORT=5432

Django allowed hosts (comma separated)

ALLOWED_HOSTS=localhost,127.0.0.1

## Other
DJANGO_SETTINGS_MODULE=project.settings

# Quick Swagger (API docs) setup recommendation
I recommend using **drf-spectacular** (clean, modern) or `drf-yasg`. Quick steps for `drf-spectacular`:

1. Install:
   ```bash
   pip install drf-spectacular


In settings.py add:
INSTALLED_APPS += ["drf_spectacular"]
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


Add URLs in urls.py:
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

## Git commands to push 
git add .
git commit -m "Final backend project submission"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
