import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIARTZHBLE5KD2FPA6E',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

#Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
copy_source = {
    'Bucket': 'awsbts99',
    'Key': '*'
}

bucket = s3.Bucket('awsbts100')

bucket.copy(copy_source, '*')


# Printing the Information That the File Is Copied.
print('Single File is copied')