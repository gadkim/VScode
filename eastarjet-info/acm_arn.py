# ACM 의 ARN 추출 
# AWS 권한 만 있으면 다른 콘솔에서도 기동
import boto3
import pprint

client = boto3.client('acm', region_name='us-east-1') # ACM 서비스 와 리전을 선택

response = client.list_certificates()

val_response = response['CertificateSummaryList']  # 리전에서 사용하고 있는 ACM 리스트 추출

# pprint.pprint (val_response)
# pprint.pprint (type(val_response))

arn_list = []
for i in val_response[0:]:
    arn_certificatearn = i['CertificateArn']  # 리전에서 사용하고 있는 ACM 의 ARN 추출
    #print (arn_certificatearn)
    arn_list.append(arn_certificatearn)

pprint.pprint (arn_list)


