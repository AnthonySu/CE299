import boto
keyId = "your_aws_access_key_id"
sKeyId="your_aws_secret_key_id"
conn = boto.connect_s3(keyId,sKeyId)
srcBucket = conn.get_bucket('mybucket001') #Source Bucket Object
dstBucket = conn.get_bucket('mybucket002') #Destination Bucket Object
fileName = "abc.txt"
#Call the copy_key() from destination bucket
dstBucket.copy_key(fileName,srcBucket.name,fileName)
