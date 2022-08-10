# IP 의 인스턴스 ID 를 검색해서 State, Tags, Platform 검색
# 1개의 Private IP 로 해당서버의 State, Tags, Platform 검색
# IP 가 여러개 있을경우 대표 IP 1개로만 확인 되어 검색이 잘되지 않음
# 이스타나 항공 기준으로 만들어서 다른 콘솔에서 실행할려면 VPC CIDR 변경 필요
import boto3
import pprint
import ipaddress

check_ip = input('IP 를 입력하세요 : ')

vpc_seoul =[]
for i in ipaddress.IPv4Network('10.222.0.0/16'):
    ip_list = str(i)
    vpc_seoul.append(ip_list)

if check_ip in vpc_seoul:
    print('======= 리전 : 서울 =======')
    ec2_list_ip_ap_northeast_2 = []
    ec2 = boto3.resource('ec2', region_name='ap-northeast-2')
    for instance in ec2.instances.all():
        list_instance = instance.id
        ec2_list_ip_ap_northeast_2.append(list_instance)

    ec2 = boto3.client('ec2', region_name='ap-northeast-2')
    for j in ec2_list_ip_ap_northeast_2[0:]:
        val_responce = ec2.describe_instances(InstanceIds = [j])
        val_responce = val_responce['Reservations']
        val_responce = val_responce[0]
        val_responce = val_responce['Instances']
        val_responce = val_responce[0]
        a = val_responce.get('PrivateIpAddress')
        b = val_responce.get('State')
        b = str(b)
        c = val_responce.get('Tags')
        c = str(c)
        last_1 = (a, 'State = ' + b, 'Tags = ' + c)
        if last_1[0] == check_ip:
            print (last_1)
            break

vpc_tokyo =[]
for i in ipaddress.IPv4Network('10.223.192.0/20'):
    ip_list = str(i)
    vpc_tokyo.append(ip_list)

if check_ip in vpc_tokyo:
    print('======= 리전 : 도쿄 =======')
    ec2_list_ip_ap_northeast_1 = []
    ec2 = boto3.resource('ec2', region_name='ap-northeast-1')
    for instance in ec2.instances.all():
        list_instance = instance.id
        ec2_list_ip_ap_northeast_1.append(list_instance)

    ec2 = boto3.client('ec2', region_name='ap-northeast-1')
    for j in ec2_list_ip_ap_northeast_1[0:]:
        val_responce = ec2.describe_instances(InstanceIds = [j])
        val_responce = val_responce['Reservations']
        val_responce = val_responce[0]
        val_responce = val_responce['Instances']
        val_responce = val_responce[0]
        a = val_responce.get('PrivateIpAddress')
        b = val_responce.get('State')
        b = str(b)
        c = val_responce.get('Tags')
        c = str(c)
        last_1 = (a, 'State = ' + b, 'Tags = ' + c)
        if last_1[0] == check_ip:
            print (last_1)
            break

vpc_syd =[]
for i in ipaddress.IPv4Network('10.223.208.0/20'):
    ip_list = str(i)
    vpc_syd.append(ip_list)

if check_ip in vpc_syd:
    print('======= 리전 : 시드니 =======')
    ec2_list_ip_ap_southeast_2 = []
    ec2 = boto3.resource('ec2', region_name='ap-southeast-2')
    for instance in ec2.instances.all():
        list_instance = instance.id
        ec2_list_ip_ap_southeast_2.append(list_instance)

    ec2 = boto3.client('ec2', region_name='ap-southeast-2')
    for j in ec2_list_ip_ap_southeast_2[0:]:
        val_responce = ec2.describe_instances(InstanceIds = [j])
        val_responce = val_responce['Reservations']
        val_responce = val_responce[0]
        val_responce = val_responce['Instances']
        val_responce = val_responce[0]
        a = val_responce.get('PrivateIpAddress')
        b = val_responce.get('State')
        b = str(b)
        c = val_responce.get('Tags')
        c = str(c)
        last_1 = (a, 'State = ' + b, 'Tags = ' + c)
        if last_1[0] == check_ip:
            print (last_1)
            break

