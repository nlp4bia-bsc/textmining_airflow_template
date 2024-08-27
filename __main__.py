import datetime
from airflow import DAG
from airflow.decorators import task
from textmining_airflow_template.scripts.example import (
    example_function
)
from textmining_airflow_template.environment import env

AIRFLOW_PIPELINE_NAME = 'textmining_template'
AIRFLOW_PIPELINE_DESCRIPTION = 'Template for Airflow Pipeline'

@task
def get_args(**kwargs):
    config = kwargs.get('dag_run').conf
    print(f"Config: {config}")
    return (
        config.get('arguments', [])
    )

with DAG(
    AIRFLOW_PIPELINE_NAME,
    start_date=datetime.datetime(2024, 5, 10),
    schedule_interval=None,
    description=AIRFLOW_PIPELINE_DESCRIPTION,
) as dag:
    arguments = get_args()
    example_arguments = example_function(arguments)
