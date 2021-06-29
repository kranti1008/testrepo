from airflow import DAG
#from airflow.operators.bash_operator import BashOperator
from airflow.operators.s3_file_transform_operator import S3FileTransformOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
from dags3 import S3COPYOPERATOR

dag = DAG('s3filecopy_dag', description='file copy from s3',
          start_date=datetime(2020, 11, 26), schedule_interval=None, catchup=False, tags=["s3 copy"])


dummy_task = PythonOperator(task_id='s3copy', provide_context=True, dag=dag)

s3copy_task = S3COPYOPERATOR(task_id=f's3_copy_process',dag=dag)


dummy_task >> s3copy_task

s3copyoperator