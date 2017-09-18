import boto
from boto.s3.key import Key
keyId = "your_aws_access_key"
sKeyId = "your_aws_secret_key"
srcFileName="abc.txt" #Name of the file to be deleted
bucketName="mybucket001" #Name of the bucket, where the file resides
conn = boto.connect_s3(keyId,sKeyId) #Connect to S3
bucket = conn.get_bucket(bucketName) #Get the bucket object
k = Key(bucket,srcFileName) #Get the key of the given object
k.delete() #Delete the object
