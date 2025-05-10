from google.cloud import bigquery
from google.cloud import storage
import os

# Configuration
BUCKET_NAME = 'abc-dev-cicd-test'
FILE_NAME = 'sample.csv'
DATASET_ID = 'people'
TABLE_ID = 'people_info'

def load_csv_to_bq():
    bq_client = bigquery.Client()
    uri = f'gs://{BUCKET_NAME}/{FILE_NAME}'

    table_ref = bq_client.dataset(DATASET_ID).table(TABLE_ID)
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    load_job = bq_client.load_table_from_uri(
        uri, table_ref, job_config=job_config
    )

    print("Starting job:", load_job.job_id)
    load_job.result()
    print("Job finished.")

    destination_table = bq_client.get_table(table_ref)
    print(f"Loaded {destination_table.num_rows} rows into {DATASET_ID}:{TABLE_ID}.")

if __name__ == '__main__':
    load_csv_to_bq()
