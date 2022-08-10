# IP-test.xlsx 파일에 A2 부터 IP 를 추가하여 리전, IP, State, Tags, Flatform 을 추출
# 이스타나 항공 기준으로 만들어서 다른 콘솔에서 실행할려면 VPC CIDR 변경 필요
# IP 가 여러개 있을경우 대표 IP 1개로만 확인 되어 검색이 잘되지 않음.
import boto3
import pprint
import ipaddress
import pandas as pd
import openpyxl
import sys

abc = []
a = pd.read_excel('IP-test.xlsx', sheet_name= 'Sheet1', usecols = 'A')      # 검색 하고자 하는 엑셀 파일 의 첫번째 시트 에 A열 기준
b = a['IP']     # A1 의 IP 텍스트
b = b.values.tolist()
ip_list_ip = b
for ip in ip_list_ip[0:]:
    check_ip = ip
    vpc_syd =[]
    for i in ipaddress.IPv4Network('10.223.208.0/20'):      # 시드리 리전의 VPC IP
        ip_list = str(i)
        vpc_syd.append(ip_list)

    if check_ip in vpc_syd:
        print('======= 리전 : 시드니 =======')
        client = boto3.client('ec2', region_name='ap-southeast-2')
        response = client.describe_instances()
        val_responce = response['Reservations']
        for i in val_responce[0:]:
            val_responce = i
            val_responce = val_responce['Instances']
            val_responce = val_responce[0]
            a = val_responce.get('PrivateIpAddress')
            b = val_responce.get('State')
            b = str(b)
            c = val_responce.get('Tags')
            c = str(c)
            d = val_responce.get('PlatformDetails')
            last_1 = (a, 'State = ' + b, 'Tags = ' + c, 'Platform = ' + d)
            if last_1[0] == check_ip:
                pprint.pprint (last_1)
                break

    vpc_tokyo =[]
    for i in ipaddress.IPv4Network('10.223.192.0/20'):      # 도쿄 리전 VPC IP
        ip_list = str(i)
        vpc_tokyo.append(ip_list)

    if check_ip in vpc_tokyo:
        print('======= 리전 : 도쿄 =======')
        client = boto3.client('ec2', region_name='ap-northeast-1')
        response = client.describe_instances()
        val_responce = response['Reservations']
        for i in val_responce[0:]:
            val_responce = i
            val_responce = val_responce['Instances']
            val_responce = val_responce[0]
            a = val_responce.get('PrivateIpAddress')
            b = val_responce.get('State')
            b = str(b)
            c = val_responce.get('Tags')
            c = str(c)
            d = val_responce.get('PlatformDetails')
            last_1 = (a, 'State = ' + b, 'Tags = ' + c, 'Platform = ' + d)
            if last_1[0] == check_ip:
                pprint.pprint (last_1)
                break

    vpc_seoul =[]
    for i in ipaddress.IPv4Network('10.222.0.0/16'):        # 서울 리전 VPC IP
        ip_list = str(i)
        vpc_seoul.append(ip_list)

    if check_ip in vpc_seoul:
        print('======= 리전 : 서울 =======')
        client = boto3.client('ec2', region_name='ap-northeast-2')
        response = client.describe_instances()
        val_responce = response['Reservations']
        for i in val_responce[0:]:
            val_responce = i
            val_responce = val_responce['Instances']
            val_responce = val_responce[0]
            a = val_responce.get('PrivateIpAddress')
            b = val_responce.get('State')
            b = str(b)
            c = val_responce.get('Tags')
            c = str(c)
            d = val_responce.get('PlatformDetails')
            last_1 = (a, 'State = ' + b, 'Tags = ' + c, 'Platform = ' + d)
            if last_1[0] == check_ip:
                pprint.pprint (last_1)
                break
        