import boto
keyId = "your_aws_access_key_id"
sKeyId= "your_aws_secret_key_id"
conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.delete_bucket('mybucket002')
