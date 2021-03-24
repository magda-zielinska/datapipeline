from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    'wait_for_downstream': True,
    "start_date": datetime(2010, 1, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG("adventures_overflow", default_args=default_args,
          schedule_interval="0 0 * * *", max_active_runs=1)

end_of_data_pipeline = DummyOperator(task_id='end_of_data_pipeline', dag=dag)

end_of_data_pipeline
