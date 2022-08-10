# ACM 에서 사용하고 있는 Domain 과 Inuse 를 추출
# AWS 권한 만 있으면 다른 콘솔에서도 기동
import boto3
import pprint

client = boto3.client('acm', region_name='ap-northeast-2')       # Acm 리전 확인

response_list = client.list_certificates()      # certificates 리스트 가져오기

val_list_response = response_list['CertificateSummaryList']     # CertificateSummaryList 값 가져오기

arn_list = []
for i in val_list_response[0:]:     # 첫번째 부터 끝까지 자동 수행
    arn_certificatearn = i['CertificateArn']        # CertificateArn 값 가져오기
    arn_list.append(arn_certificatearn)     # 리스트 형식으로 Arn 값 가져오기

# pprint.pprint (arn_list)
for j in arn_list[0:]:
    response = client.describe_certificate(
        CertificateArn = j
    )
    val_response = response['Certificate']
    # pprint.pprint (val_response)
    val_InUseBy_response = val_response['InUseBy']  # ACM 의 사용하고 있는 Resource 추출
    val_DomainName_response = val_response['DomainName']  # ACM 에 등록된 Domain 추출
    pprint.pprint (val_DomainName_response)
    pprint.pprint (val_InUseBy_response)