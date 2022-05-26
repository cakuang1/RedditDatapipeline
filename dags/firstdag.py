from asyncio import tasks
from json import load
from tracemalloc import start
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

from datetime import timedelta

import pandas as pd








#defining the first task. We are taking our raw data and transforming using pandas
# def trasform_data:



    



#  second task
# def load_data:





#     return














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











