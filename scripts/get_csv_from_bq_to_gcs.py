from google.cloud import bigquery
# export large data from gcs as csvs without headers
table_id_bucket = {
    "citibike_stations":"test-spak/citibike_stations_export",
    "citibike_trips":"test-spak/citibike_trips_export"}

for TABLE, BUCKET in table_id_bucket.items():
    client = bigquery.Client()
    bucket_name = BUCKET

    project = 'bigquery-public-data'
    dataset_id = 'new_york_citibike'
    table_id = TABLE

    destination_uri = 'gs://{}/{}'.format(bucket_name, 'file-*.csv')
    dataset_ref = client.dataset(dataset_id, project=project)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.job.ExtractJobConfig(print_header=False)

    extract_job = client.extract_table(
        table_ref,
        destination_uri,
        # Location must match that of the source table.
        location='US',
        job_config=job_config)  # API request

    extract_job.result()  # Waits for job to complete.

    print('Exported {}:{}.{} to {}'.format(
        project, dataset_id, table_id, destination_uri))
