import os
import boto3
import time
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
import logging
log = logging.getLogger(__name__)

class S3COPYOPERATOR(BaseOperator):
    @apply_defaults
    def __init__(self, req_data, *args, **kwargs):
        super(WmsBHProcessOperator, self).__init__(*args, **kwargs)
    def execute(self, context):
        try:
            session = boto3.Session(
            aws_access_key_id='AKIARTZHBLE5KD2FPA6E',
            aws_secret_access_key='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'
            )

            today=time.strftime('%Y%m%d')

            #Creating S3 Resource From the Session.
            s3 = session.resource('s3')

            srcbucket = s3.Bucket('awsbts99')   

            destbucket = s3.Bucket('awsbts100')

            bucket_prefix="clover-vendor-sftp/convey/production/to_clover/member_evolve/"+today

            objs = srcbucket.objects.filter(Prefix = bucket_prefix)

            # Iterate All Objects in Your S3 Bucket Over the for Loop
            for obj in objs:
                path, filename = os.path.split(obj.key)    
                #Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
                copy_source = {
                'Bucket': 'awsbts99',
                'Key': obj.key
                }
                
                file_name = os.path.basename(obj.key)
                destbucket.copy(copy_source, 'clover-vendor-sftp/evolve/production/from_clover/member_evolve/'+file_name)  
                print(file_name +'- File Copied')

            
        except Exception as e: 
                log.info(f'error:{e}')


#Creating Session With Boto3.
