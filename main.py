from google.cloud import bigquery


def ex1_trigger(event, context):
    bq_project = 'alterdata-rekrutacja-1'
    bq_dataset = 'pd_ex1_dataset'
    [file_name, extension] = event['name'].split('.')
    if extension == 'csv':
        bq_client = bigquery.Client()
        bq_table = bigquery.Table('{}.{}.{}'.format(bq_project, bq_dataset, file_name))

        job_config = bigquery.LoadJobConfig(
            autodetect=True, source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1,
            write_disposition='WRITE_TRUNCATE'
        )
        csv_uri = 'gs://{}/{}.{}'.format(event['bucket'], file_name, extension)
        load_job = bq_client.load_table_from_uri(
            csv_uri, bq_table, job_config=job_config
        )
        load_job.result()
