""" " """
"""my_bucket=s3.Bucket(s3_bucket_name)
bucket_list = []
for file in my_bucket.objects.filter(Prefix = '20210626'
    file_name=file.key
    if file_name.find(".txt")!=-1:
        bucket_list.append(file.key)
length_bucket_list=print(len(bucket_list))
print(bucket_list[0:10]) """

import os
import boto3
import time

#Creating Session With Boto3.
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
