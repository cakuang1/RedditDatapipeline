import pandas as pd
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from scripts.functions import *

import pandas as pd



with DAG(
    dag_id = 
)

task_1 = PythonOperator(
    task_id = 'transform_data',
    python_callable = transform_data,
    dag = ingestiondag
)


task_2 = PythonOperator(
    task_id = 'load_data',
    python_callable = load_data,
    dag = ingestiondag
)


task_1 >> task_2











