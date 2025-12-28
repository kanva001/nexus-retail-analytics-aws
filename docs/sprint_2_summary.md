# Sprint 2 Deliverable: Silver Layer (Optimization & Transformation)

## 1. Objective
To transform raw, unorganized CSV data (Bronze) into an optimized, query-ready Parquet format (Silver) while standardizing the schema.

## 2. The "Why" (Problem Statement)
- **Performance:** CSVs are row-based and slow for large-scale queries. 
- **Storage:** CSVs are uncompressed. Parquet uses Snappy compression, saving AWS storage costs.
- **Naming Conventions:** Original SQL names (CamelCase) needed to be converted to `snake_case` for easier SQL writing in Athena.

## 3. Implementation
- **Library:** Used `pandas` and `pyarrow` for the transformation.
- **In-Memory Processing:** Utilized `io.BytesIO` to convert files without writing to local disk, making the pipeline "Cloud Native."
- **Standardization:** Programmatically converted all column headers to lowercase with underscores.

## 4. Validation
- Verified the existence of `.parquet` files in the Silver S3 bucket.
- Confirmed that the Python script correctly handled data types during the conversion process.

## 5. Security Incident & Recovery
- **Issue:** Detected sensitive AWS Access Keys pushed to the public repository in `src/.env`.
- **Response:** 1. Immediately removed the file from Git tracking using `git rm --cached`.
    2. Updated `.gitignore` to prevent future leaks.
    3. Rotated IAM credentials in the AWS Console to invalidate the leaked keys.
- **Outcome:** Pipeline is now secure and running with fresh, protected credentials.

## 6. Data Cataloging (AWS Glue)
- **Service:** AWS Glue Crawler.
- **Process:** Configured a crawler with a custom IAM Role (`AWSGlueServiceRole-NexusRetailAnalytics`) to scan the Silver bucket.
- **Result:** Successfully identified schemas and created 3 metadata tables in the `db_retail_analytics` database.

## 7. Final Results & Analytics
- **Validation Tool:** AWS Athena.
- **Success Metric:** Successfully executed SQL JOIN queries on Parquet data.
- **Key Insight:** Verified top-selling products and high-value customers directly from the S3 Lakehouse.