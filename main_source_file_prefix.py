import os
import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIARTZHBLE5KD2FPA6E',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

srcbucket = s3.Bucket('awsbts99')   

destbucket = s3.Bucket('awsbts100')

bucket_prefix="clover-vendor-sftp/convey/production/to_clover/member_evolve/20210626"

objs = srcbucket.objects.filter(Prefix = bucket_prefix)

# Iterate All Objects in Your S3 Bucket Over the for Loop
for obj in objs:
    path, filename = os.path.split(obj.key)    
    #Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
    copy_source = {
    'Bucket': 'awsbts99',
    'Key': obj.key
    }
    
    destbucket.copy(copy_source, obj.key)
    
    print(obj.key +'- File Copied')
    
    
    
    /awsbts99/clover-vendor-sftp/convey/production/to_clover/member_evolve/
    
    target s3://awsbts100/clover-vendor-sftp/evolve/production/from_clover/
    
import os 
import boto3
s3 = boto3.resource('s3')
mybucket = s3.Bucket("mybucket")
# if blank prefix is given, return everything)
bucket_prefix="clover-vendor-sftp/convey/production/to_clover/member_evolve/20210626"
objs = mybucket.objects.filter(Prefix = bucket_prefix)

for obj in objs:
    path, filename = os.path.split(obj.key)
    # boto3 s3 download_file will throw exception if folder not exists
    try:
        os.makedirs(path) 
    except FileExistsError:
        pass
    mybucket.download_file(obj.key, obj.key)