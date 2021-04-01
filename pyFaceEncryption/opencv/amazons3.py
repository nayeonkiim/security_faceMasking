# %%
import os
import csv
import boto3
from botocore.exceptions import ClientError

# 암호 파일
csv_file = open('C:/rootkey.csv', 'r', encoding='utf-8')
csv_read = csv.reader(csv_file)
read_data = []
for line in csv_read:
    read_data.append(line)
csv_file.close()

# IAM 유저 생성 후 받은 키 입력
my_id = read_data[1][2]
my_key = read_data[1][3]

# %%
def create_s3_bucket(bucket_name):
    print("Creating a bucket... " + bucket_name)

    s3 = boto3.client(
        's3',  # 사용할 서비스 이름, ec2이면 'ec2', s3이면 's3', dynamodb이면 'dynamodb'
        aws_access_key_id=my_id,  # 액세스 ID
        aws_secret_access_key=my_key)  # 비밀 엑세스 키

    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-northeast-2'  # Seoul  # us-east-1을 제외한 지역은 LocationConstraint 명시해야함.
            }
        )
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print("Bucket already exists. skipping..")
        else:
            print(e)
            print("Unknown error, exit..")


