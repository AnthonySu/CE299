import boto
from boto.s3.key import Key
keyId ="your_aws_key_id"
sKeyId="your_aws_secret_key_id"
srcFileName="abc.txt"
destFileName="s3_abc.txt"
bucketName="mybucket001"
conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.get_bucket(bucketName)
#Get the Key object of the given key, in the bucket
k = Key(bucket,srcFileName)
#Get the contents of the key into a file 
k.get_contents_to_filename(destFileName)
