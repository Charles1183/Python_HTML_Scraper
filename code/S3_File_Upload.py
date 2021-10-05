import logging
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
import os



s3 = boto3.client('s3')
#response = s3.list_buckets()
local_file = '' #Local file location
s3_file = '' #new file name for S3 object
bucket = '' #bucket name

try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
except FileNotFoundError:
        print("The file was not found")
except NoCredentialsError:
        print("Credentials not available")


#print('Existing buckets:')
#for bucket in response['Buckets']:
#    print(f'  {bucket["Name"]}')

