from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print('Hello World')

# with DAG(dag_id='hello_wordl_dag',
#          start_date=datetime(2021,1,1),
#          schedule_intervals='@hourly',
#          catchup=False) as dag: