import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

# [START howto_operator_python]
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)
        
    python_task_1 = print_context('task decorator 실행')

