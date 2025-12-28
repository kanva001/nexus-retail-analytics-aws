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
- Verified the existence of `.parquet` files in `s3://nexus-retail-silver-.../`.
- Successfully ignored local `venv` and `.env` files during the Git push to maintain repository security.

## 7. Final Validation & Results
- **AWS Glue:** Created and executed a crawler to catalog 3 tables into the `db_retail_analytics` database.
- **Athena Integration:** Successfully executed SQL JOIN queries on Parquet data.
- **Key Result:** Data is now accessible for BI tools (like Power BI or Tableau) with optimized performance.