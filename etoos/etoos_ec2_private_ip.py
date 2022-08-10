import boto3
import pprint
import ipaddress
from boto3.session import Session

# client = boto3.client('ec2')
# response = client.describe_network_interfaces()
# pprint.pprint(response)

check_ip = input('IP 를 입력하세요 : ')

session = boto3.Session(profile_name = 'etoosmainaccount')
client = session.client('ec2')
response = client.describe_network_interfaces()
val_responce = response['NetworkInterfaces']
for i in val_responce[0:]:
    val_responce = i
    # pprint.pprint(val_responce)
    a = val_responce.get('Description')
    b = val_responce.get('PrivateIpAddress')
    c = val_responce.get('Association')
    d = val_responce.get('Groups')
    if b == check_ip:
        print('Account : 994185550341 (ETOOS Main Account)')
        print('Description : ' + a)
        print('PrivateIpAddress : ' + b)
        print('Association : ' + str(c))
        print('Security Group :' + str(d))
        break

session = boto3.Session(profile_name = 'aiddev')
client = session.client('ec2')
response = client.describe_network_interfaces()
val_responce = response['NetworkInterfaces']
for i in val_responce[0:]:
    val_responce = i
    # pprint.pprint(val_responce)
    a = val_responce.get('Description')
    b = val_responce.get('PrivateIpAddress')
    c = val_responce.get('Association')
    d = val_responce.get('Groups')
    if b == check_ip:
        print('Account : 196859722530 (aid-dev)')
        print('Description : ' + a)
        print('PrivateIpAddress : ' + b)
        print('Association : ' + str(c))
        print('Security Group :' + str(d))
        break

session = boto3.Session(profile_name = 'aidprod')
client = session.client('ec2')
response = client.describe_network_interfaces()
val_responce = response['NetworkInterfaces']
for i in val_responce[0:]:
    val_responce = i
    # pprint.pprint(val_responce)
    a = val_responce.get('Description')
    b = val_responce.get('PrivateIpAddress')
    c = val_responce.get('Association')
    d = val_responce.get('Groups')
    if b == check_ip:
        print('Account : 927429525761 (aid-prod)')
        print('Description : ' + a)
        print('PrivateIpAddress : ' + b)
        print('Association : ' + str(c))
        print('Security Group :' + str(d))
        break

session = boto3.Session(profile_name = 'cpoplatform')
client = session.client('ec2')
response = client.describe_network_interfaces()
val_responce = response['NetworkInterfaces']
for i in val_responce[0:]:
    val_responce = i
    # pprint.pprint(val_responce)
    a = val_responce.get('Description')
    b = val_responce.get('PrivateIpAddress')
    c = val_responce.get('Association')
    d = val_responce.get('Groups')
    if b == check_ip:
        print('Account : 196235754137 (cpo-platform)')
        print('Description : ' + a)
        print('PrivateIpAddress : ' + b)
        print('Association : ' + str(c))
        print('Security Group :' + str(d))
        break