# Project Nexus: Enterprise Retail 360
## Business Requirements & Architectural Blueprint

### 1. Project Overview
A cloud-native ETL pipeline that transforms raw SQL Server transactional data into actionable business intelligence. It utilizes a **Medallion Architecture** (Bronze/Silver/Gold) to ensure data quality, auditability, and scalability.

### 2. The Architectural Blueprint
The pipeline transitions data from a local on-premise environment to a modern AWS stack:
* **Extraction:** Local SQL Server → AWS S3 (Raw/Bronze) via Python/Boto3.
* **Transformation (ETL):** Python/Pandas & AWS Glue.
* **Storage:** Amazon S3 (Optimized Parquet format).
* **Data Catalog:** AWS Glue Data Catalog.
* **Analysis:** Amazon Athena (Serverless SQL).

### 3. Requirements & User Stories
To ensure production-grade standards, the following requirements were met:
* **Requirement 1:** Automated ingestion of Sales, Product, and Customer tables.
* **Requirement 2:** Data cleaning (handling NULLs and standardizing date formats).
* **Requirement 3:** Schema Evolution (ensuring the pipeline remains resilient to source changes).
* **Requirement 4:** Data Validation (ensuring record integrity across layers).

### 4. Progressive Deployment Plan (Agile Sprints)
| Sprint | Goal | AWS Services |
| :--- | :--- | :--- |
| **Sprint 1** | The Landing Zone | S3, IAM, Python |
| **Sprint 2** | The Silver Layer | Pandas, Parquet, S3 |
| **Sprint 3** | The Gold Layer | Glue, Athena, SQL |
| **Sprint 4** | DevOps & Security | Git Security, .env, Documentation |