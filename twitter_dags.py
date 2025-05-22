from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator  # updated import for Airflow 2+
from twitter_etl import run_twitter_etl

# Default arguments for the DAG's tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 22),  # use a recent date for first run
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    dag_id='twitter_dag',
    default_args=default_args,
    description='A DAG to run a Twitter ETL pipeline daily.',
    schedule_interval=timedelta(days=1),  # daily interval
    catchup=False,  # avoids backfilling from start_date
    tags=['twitter', 'etl'],  # optional but helpful for UI filtering
) as dag:

    # Define the Python task
    run_etl = PythonOperator(
        task_id='complete_twitter_etl',
        python_callable=run_twitter_etl
    )

    run_etl
