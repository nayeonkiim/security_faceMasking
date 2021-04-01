# 파일 올리기
import os
import glob
import boto3
import amazons3

def fileUpToS3(input_path):
    splited = input_path.split('/')
    stored_names = splited[len(splited)-1]
    print(stored_names)

    s3 = boto3.client(
        's3',  # 사용할 서비스 이름, ec2이면 'ec2', s3이면 's3', dynamodb이면 'dynamodb'
        aws_access_key_id=amazons3.my_id,  # 액세스 ID
        aws_secret_access_key=amazons3.my_key)  # 비밀 엑세스 키
    s3.upload_file(input_path, "버킷이름", stored_names)



# reference: https://assaeunji.github.io/aws/2020-04-02-boto3/