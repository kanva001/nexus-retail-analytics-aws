# Sprint 3 Deliverable: Gold Layer & Business Intelligence

## 1. Objective
To transform the normalized Silver data into a "Business-Ready" format for reporting and analytics.

## 2. Implementation
- **Architecture:** Created a SQL View in AWS Athena.
- **Logic:** Joined `factinternetsales` with `dimproduct` and `dimcustomer` to remove technical keys and provide human-readable names.
- **Optimization:** Utilized the existing Parquet format for high-performance scanning.

## 3. Project Conclusion
- **Bronze:** Successfully ingested raw CSV data from SQL Server to S3.
- **Silver:** Converted data to Parquet using Python (Pandas/Boto3) with standardized naming.
- **Gold:** Created a queryable semantic layer for end-users.