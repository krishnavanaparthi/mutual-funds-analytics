# Mutual Funds Analytics ETL Pipeline

## Overview

This capstone project builds a complete ETL pipeline for Indian Mutual Fund analytics.

## Data Sources

- MFAPI
- AMFI India

## Technologies

- Python
- Pandas
- NumPy
- Requests
- SQLite
- Plotly
- Jupyter

## Project Structure

```
data/
raw/
processed/

scripts/

reports/

dashboard/

sql/
```

## Day 1 Completed

- Project Setup
- Data Ingestion
- Live NAV Download
- AMFI Download
- Data Exploration
- Validation

## Day 2 Completed

### Data Cleaning and Transformation

* Cleaned all mentor-provided datasets and saved processed files in `data/processed/`
* Converted date columns to proper datetime format
* Removed duplicate records where applicable
* Validated NAV values and ensured positive values
* Standardized transaction data and validated KYC status values
* Validated scheme performance metrics and expense ratio ranges
* Generated cleaned datasets for downstream analysis

### Database Development

* Created SQLite database: `bluestock_mf.db`
* Connected SQLite using SQLAlchemy
* Loaded cleaned datasets into the database
* Verified database row counts against source CSV files

### Schema Design

* Designed a star schema architecture for future analytical reporting
* Created `schema.sql` containing:

  * `dim_fund`
  * `dim_date`
  * `fact_nav`
  * `fact_transactions`
  * `fact_performance`
  * `fact_aum`
* Defined primary keys and foreign key relationships

### SQL Analytics

* Created 10 analytical SQL queries in `queries.sql`
* Implemented queries for:

  * Top funds by AUM
  * Average NAV analysis
  * SIP growth analysis
  * Transaction analysis by state
  * Expense ratio analysis
  * Fund performance analysis
  * Category-wise insights

### Documentation

* Created Data Dictionary (`reports/data_dictionary.md`)
* Documented dataset columns, data types, and business definitions
* Created Data Quality Summary report
* Added SQL schema and query documentation

### Deliverables Completed

* 10 cleaned CSV files
* SQLite database (`bluestock_mf.db`)
* Schema definition file (`schema.sql`)
* Data loading script (`load_database.py`)
* Database validation script (`verify_database.py`)
* SQL query collection (`queries.sql`)
* Data dictionary (`data_dictionary.md`)

### Technologies Used

* Python
* Pandas
* SQLite
* SQLAlchemy
* Git & GitHub

Status: ✅ Day 2 Successfully Completed
