import boto3
#s3 = boto3.client('s3',region_name='us-east-1')
#s3.create_bucket(Bucket='my-bucket-sssssseee45')
#import boto3
ec2 = boto3.resource('ec2',region_name='us-east-1')
# create VPC
vpc = ec2.create_vpc(CidrBlock='172.31.0.0/16')
#assign a name to our VPC
vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc5"}])
vpc.wait_until_available()
###
