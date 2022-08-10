# 1개의 Private IP 로 해당서버의 State, Tags, Platform 검색
# IP 가 여러개 있을경우 대표 IP 1개로만 확인 되어 검색이 잘되지 않음
# 이스타나 항공 기준으로 만들어서 다른 콘솔에서 실행할려면 VPC CIDR 변경 필요
import boto3
import pprint
import ipaddress

check_ip = input('IP 를 입력하세요 : ')

vpc_syd =[]
for i in ipaddress.IPv4Network('10.223.208.0/20'):   # 시드니 VPC CIDR
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
for i in ipaddress.IPv4Network('10.223.192.0/20'):  # 도쿄 VPC CIDR
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
for i in ipaddress.IPv4Network('10.222.0.0/16'):  # 서울 VPC CIDR
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
