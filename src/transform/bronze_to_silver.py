import pandas as pd
import boto3
import io
import os
from dotenv import load_dotenv

load_dotenv()

def transform_bronze_to_silver():
    s3 = boto3.client('s3')
    
    source_bucket = os.getenv('AWS_BUCKET_BRONZE')
    target_bucket = os.getenv('AWS_BUCKET_SILVER')
    
    tables = ['FactInternetSales', 'DimCustomer', 'DimProduct']

    for table in tables:
        print(f"--- Processing {table} ---")
        
        # 1. READ from Bronze
        response = s3.get_object(Bucket=source_bucket, Key=f"bronze/{table}/{table}.csv")
        df = pd.read_csv(io.BytesIO(response['Body'].read()))

        # 2. TRANSFORM: Standardize names (Lower case and underscore)
        df.columns = [c.lower().replace(' ', '_') for c in df.columns]
        
        # 3. CONVERT & WRITE to Silver as Parquet
        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer, index=False)
        
        target_key = f"silver/{table}/{table}.parquet"
        s3.put_object(
            Bucket=target_bucket, 
            Key=target_key, 
            Body=parquet_buffer.getvalue()
        )
        print(f"Successfully moved {table} to Silver Layer.")

if __name__ == "__main__":
    transform_bronze_to_silver()