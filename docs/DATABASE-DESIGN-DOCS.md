# HubSpot Deals Database Schema

## Overview
This document defines the PostgreSQL schema for storing HubSpot Deals data for the ETL pipeline.  
The design supports multi-tenant data isolation, ETL metadata tracking, and efficient querying.

## Table: deals

| Column Name | Data Type       | Description |
|-------------|----------------|-------------|
| deal_id     | BIGINT PRIMARY KEY | HubSpot Deal ID |
| tenant_id   | VARCHAR(50)    | Tenant identifier for multi-tenant isolation |
| deal_name   | TEXT           | Name of the deal |
| amount      | NUMERIC(15,2)  | Deal amount |
| pipeline    | VARCHAR(50)    | Pipeline the deal belongs to |
| stage       | VARCHAR(50)    | Current stage of the deal |
| owner_id    | BIGINT          | HubSpot owner ID |
| created_at  | TIMESTAMP       | Deal creation date/time |
| updated_at  | TIMESTAMP       | Last update date/time |
| closed_at   | TIMESTAMP       | Close date/time (if applicable) |
| is_deleted  | BOOLEAN         | Soft delete flag (archived) |

### ETL Metadata Columns
| Column Name  | Data Type | Description |
|-------------|-----------|-------------|
| extracted_at | TIMESTAMP | Timestamp when ETL extracted the data |
| scan_id      | UUID      | Unique ETL batch identifier |
| loaded_at    | TIMESTAMP | Timestamp when data was loaded into database |

## CREATE TABLE Statement
```sql
CREATE TABLE deals (
    deal_id BIGINT PRIMARY KEY,
    tenant_id VARCHAR(50) NOT NULL,
    deal_name TEXT,
    amount NUMERIC(15,2),
    pipeline VARCHAR(50),
    stage VARCHAR(50),
    owner_id BIGINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    closed_at TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    extracted_at TIMESTAMP,
    scan_id UUID,
    loaded_at TIMESTAMP
);
CREATE INDEX idx_deals_tenant ON deals(tenant_id);
CREATE INDEX idx_deals_created_at ON deals(created_at);
CREATE INDEX idx_deals_closed_at ON deals(closed_at);
CREATE INDEX idx_deals_stage ON deals(stage);
