import boto
keyId = "your_aws_access_key_id"
sKeyId= "your_aws_secret_key_id"
bucketName="mybucket002"
conn = boto.connect_s3(keyId,sKeyId) #Connect to S3
bucket = conn.get_bucket(bucketName) #Get the bucket Object
for i in bucket.list():
 print(i.key)
 i.delete() #Delete the object
