import boto
from boto.s3.key import Key
keyId = "your_aws_key_id"
sKeyId= "your_aws_secret_key_id"
fileName="abcd.txt"
bucketName="mybucket001"
file = open(fileName)
conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.get_bucket(bucketName)
#Get the Key object of the bucket
k = Key(bucket)
#Crete a new key with id as the name of the file
k.key=fileName
#Upload the file
result = k.set_contents_from_file(file)
#result contains the size of the file uploaded
