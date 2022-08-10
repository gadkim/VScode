# ACM 의 ARN 으로 ACM 에서 사용하고 있는 Resource 를 확인
# AWS 권한 만 있으면 다른 콘솔에서도 기동
import boto3
import json

client = boto3.client('acm', region_name='us-east-1') # ACM 서비스 와 리전을 선택

response = client.describe_certificate(
    CertificateArn='arn:aws:acm:us-east-1:612830199036:certificate/bdc19623-2402-46be-ba78-3395f1148d7c'  # ACM 의 ARN 을 기재
)

val_response = response['Certificate']  # 필더 링 과정

val_1_response = val_response['InUseBy'] # 사용 하고 이는 서비스 를 리스트로 추출

print (val_1_response)

