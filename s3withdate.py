import boto3
import time

#print time.strftime('%Y%m%d')
prefix =time.strftime('%Y%m%d') 
file_name='{prefix}_Member_Profile.txt'

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIARTZHBLE5KD2FPA6E',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

srcbucket = s3.Bucket('awsbts99')

destbucket = s3.Bucket('awsbts100')

# Iterate All Objects in Your S3 Bucket Over the for Loop
for file in srcbucket.objects.all():
    
    #Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
    copy_source = {
    'Bucket': 'awsbts99',
    'Key': 'clover-vendor-sftp/convey/production/to_clover/member_evolve/123.txt'
    }
    
    destbucket.copy(copy_source, '123.txt')
    
    print('clover-vendor-sftp/convey/production/to_clover/member_evolve/123.txt' +'- File Copied')
    
    
    
    /awsbts99/clover-vendor-sftp/convey/production/to_clover/member_evolve/
    
import boto3
s3_resource = boto3.resource('s3')
# Copy object A as object B
s3_resource.Object("awsbts100", "newpath/to/object_B.txt").copy_from(
 CopySource=”/awsbts99/clover-vendor-sftp/convey/production/to_clover/member_evolve/*.txt”)