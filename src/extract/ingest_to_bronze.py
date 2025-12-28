import os
import pandas as pd
import boto3
from sqlalchemy import create_engine
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env
load_dotenv()

def ingest_retail_data():
    # 1. Configuration from .env
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    bucket = os.getenv('AWS_BUCKET_NAME')
    
    # 2. Setup Connection String (Windows Authentication)
    # Note: Using 'ODBC Driver 17 for SQL Server' - ensure this is installed on your Win 11 PC
    conn_str = f"mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    engine = create_engine(conn_str)

    # 3. List of tables we want to extract from AdventureWorksDW
    tables = ['FactInternetSales', 'DimCustomer', 'DimProduct']

    # 4. Initialize AWS S3 Client
    s3_client = boto3.client('s3')

    for table in tables:
        try:
            print(f"--- Starting Extraction for {table} ---")
            
            # Extract
            df = pd.read_sql(f"SELECT * FROM {table}", engine)
            
            # Add Metadata: Record when this data was extracted
            df['extraction_timestamp'] = datetime.now()
            
            # Define file paths
            local_file = f"{table}.csv"
            s3_key = f"bronze/{table}/{table}.csv"
            
            # Save locally (temporary)
            df.to_csv(local_file, index=False)
            
            # Upload to S3
            print(f"Uploading {table} to s3://{bucket}/{s3_key}...")
            s3_client.upload_file(local_file, bucket, s3_key)
            
            # Cleanup local file
            os.remove(local_file)
            print(f"Successfully ingested {table}")

        except Exception as e:
            print(f"Error ingesting {table}: {e}")

if __name__ == "__main__":
    ingest_retail_data()