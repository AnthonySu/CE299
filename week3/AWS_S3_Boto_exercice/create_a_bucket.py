import boto
keyId = "your_aws_key_id"
sKeyId="your_aws_secret_key_id"
#Connect to S3 with access credentials 
conn = boto.connect_s3(keyId,sKeyId) 
#Create the bucket in a specific region.
bucket = conn.create_bucket('mybucket001',location='us-west-2')
