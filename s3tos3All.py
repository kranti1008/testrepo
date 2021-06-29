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

# Iterate All Objects in Your S3 Bucket Over the for Loop
for file in srcbucket.objects.all():
    
    #Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
    copy_source = {
    'Bucket': 'awsbts99',
    'Key': file.key
    }
    
    destbucket.copy(copy_source, file.key)
    
    print(file.key +'- File Copied')