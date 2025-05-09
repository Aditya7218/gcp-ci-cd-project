# GCP CI/CD Pipeline Example

This project demonstrates a simple CI/CD pipeline on Google Cloud using:

- GitHub + Cloud Build
- Cloud Storage (GCS) for source files
- BigQuery as the destination

### How It Works

1. A CSV file is uploaded to a GCS bucket.
2. A Python script loads that CSV into a BigQuery table.
3. Cloud Build automatically runs the script when code is pushed.

### Prerequisites

- GCS bucket and BigQuery dataset/table created
- Cloud Build trigger set up on GitHub push
