# EC2 의 모든 정보 추출
# 정보가 많아 .txt 로 만들어서 데이터 확인 ec2_describe.py > ec2-describe.txt
import boto3
import pprint

client = boto3.client('ec2', region_name='ap-southeast-2')
response = client.describe_snapshots()

pprint.pprint (response)