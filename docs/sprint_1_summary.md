# Sprint 1 Deliverable: Data Ingestion (Bronze Layer)

## 1. Project Overview
**Objective:** Build a hybrid cloud pipeline to move retail data from an on-premise SQL Server (AdventureWorksDW) to an AWS S3 Data Lake.

## 2. Problem Statement
The business required a way to perform heavy analytical queries without impacting the performance of the live transactional SQL Server. We needed a scalable "Landing Zone" for raw data.

## 3. Implementation Details
- **Extraction:** Used Python (`pandas`, `sqlalchemy`) to pull data from SQL Server.
- **Loading:** Utilized `boto3` to stream data into AWS S3 (Bronze Bucket).
- **Security:** Implemented environment variables (`.env`) to protect AWS credentials and managed a `.gitignore` to prevent leaks.
- **Data Governance:** Added `extraction_timestamp` to all records for lineage tracking.

## 4. Challenges & Solutions
| Challenge | Solution |
| :--- | :--- |
| **ODBC Driver Errors** | Installed and configured ODBC Driver 17 for SQL Server on Windows 11. |
| **Secret Leaks** | Used `git reset` to unstage `.env` files and updated `.gitignore`. |
| **Line Endings (LF/CRLF)** | Configured Git to handle Windows-style line endings without disrupting the repo. |

## 5. Outcome
Successfully moved 3 key tables (**FactInternetSales**, **DimCustomer**, **DimProduct**) to `s3://[Your-Bronze-Bucket-Name]/bronze/` in CSV format.