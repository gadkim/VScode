# 특정 IP 가 VPC CIDR 에 포함되면 무족건 검색
# 리전, 서브넷 대역 확인 시 사용되며 출력 내용을 수동으로 입력 하는 방식이라 주의사항 및 특이사항을 기재가능
import ipaddress

etoos_ip = input('IP 를 넣어주세요 : ')

# etoos-main
prod_vpc_01 =[]
for i in ipaddress.IPv4Network('172.19.0.0/16'):
    ip_list = str(i)
    prod_vpc_01.append(ip_list)

com_vpc_01 =[]
for i in ipaddress.IPv4Network('172.20.0.0/16'):
    ip_list = str(i)
    com_vpc_01.append(ip_list)

dev_vpc_01 =[]
for i in ipaddress.IPv4Network('192.168.0.0/16'):
    ip_list = str(i)
    dev_vpc_01.append(ip_list)

api_prod_vpc01 =[]
for i in ipaddress.IPv4Network('172.18.0.0/22'):
    ip_list = str(i)
    api_prod_vpc01.append(ip_list)

sso_prod_vpc01 =[]
for i in ipaddress.IPv4Network('172.18.4.0/22'):
    ip_list = str(i)
    api_prod_vpc01.append(ip_list)

test_vpc_01 =[]
for i in ipaddress.IPv4Network('10.245.0.0/16'):
    ip_list = str(i)
    test_vpc_01.append(ip_list)

# =============================================================
# etoos-aid-prod
edl_alpha_vpc01 =[]
for i in ipaddress.IPv4Network('172.18.9.0/24'):
    ip_list = str(i)
    edl_alpha_vpc01.append(ip_list)

edl_prod_vpc01 =[]
for i in ipaddress.IPv4Network('172.18.8.0/24'):
    ip_list = str(i)
    edl_prod_vpc01.append(ip_list)

# =============================================================
# etoos-cpo-platform
vpc_com =[]
for i in ipaddress.IPv4Network('172.25.0.0/20'):
    ip_list = str(i)
    vpc_com.append(ip_list)

vpc_com_prd_1 =[]
for i in ipaddress.IPv4Network('172.25.130.0/23'):
    ip_list = str(i)
    vpc_com_prd_1.append(ip_list)

vpc_com_prd_2 =[]
for i in ipaddress.IPv4Network('172.25.129.0/24'):
    ip_list = str(i)
    vpc_com_prd_2.append(ip_list)

vpc_dev =[]
for i in ipaddress.IPv4Network('172.25.16.0/20'):
    ip_list = str(i)
    vpc_dev.append(ip_list)

vpc_stg =[]
for i in ipaddress.IPv4Network('172.25.64.0/20'):
    ip_list = str(i)
    vpc_stg.append(ip_list)

vpc_mgmt_prd =[]
for i in ipaddress.IPv4Network('172.25.104.0/21'):
    ip_list = str(i)
    vpc_mgmt_prd.append(ip_list)

vpc_perf =[]
for i in ipaddress.IPv4Network('172.25.48.0/20'):
    ip_list = str(i)
    vpc_perf.append(ip_list)

vpc_prd =[]
for i in ipaddress.IPv4Network('172.25.112.0/20'):
    ip_list = str(i)
    vpc_prd.append(ip_list)

vpc_qa =[]
for i in ipaddress.IPv4Network('172.25.32.0/20'):
    ip_list = str(i)
    vpc_qa.append(ip_list)

vpc_sand =[]
for i in ipaddress.IPv4Network('172.25.80.0/20'):
    ip_list = str(i)
    vpc_sand.append(ip_list)

# =============================================================
# etoos-aid-dev
edl_dev_vpc01 =[]
for i in ipaddress.IPv4Network('172.17.3.0/24'):
    ip_list = str(i)
    edl_dev_vpc01.append(ip_list)

# =============================================================
# etoos_office
etoos_office_1 =[]
for i in ipaddress.IPv4Network('10.10.100.0/23'):
    ip_list = str(i)
    etoos_office_1.append(ip_list)

etoos_office_2 =[]
for i in ipaddress.IPv4Network('10.20.25.0/24'):
    ip_list = str(i)
    etoos_office_2.append(ip_list)

etoos_office_3 =[]
for i in ipaddress.IPv4Network('10.20.30.0/24'):
    ip_list = str(i)
    etoos_office_3.append(ip_list)

etoos_office_4 =[]
for i in ipaddress.IPv4Network('10.20.35.0/24'):
    ip_list = str(i)
    etoos_office_4.append(ip_list)


if etoos_ip in prod_vpc_01:
    print ('ETOOS-Main-SEOUL / prod_vpc_01')
elif etoos_ip in com_vpc_01:
    print ('ETOOS-Main-SEOUL / com_vpc_01')
elif etoos_ip in dev_vpc_01:
    print ('ETOOS-Main-SEOUL / dev_vpc_01')
elif etoos_ip in api_prod_vpc01:
    print ('ETOOS-Main-SEOUL / api_prod_vpc01')
elif etoos_ip in sso_prod_vpc01:
    print ('ETOOS-Main-SEOUL / sso_prod_vpc01')
elif etoos_ip in test_vpc_01:
    print ('ETOOS-Main-SEOUL / test_vpc_01')
# ========
elif etoos_ip in edl_alpha_vpc01:
    print ('ETOOS-aid-prod-SEOUL / edl_alpha_vpc01')
elif etoos_ip in edl_prod_vpc01:
    print ('ETOOS-aid-prod-SEOUL / edl_prod_vpc01')
# ========
elif etoos_ip in vpc_com:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_com')
elif etoos_ip in vpc_com_prd_1:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_com_prd_1')
elif etoos_ip in vpc_com_prd_2:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_com_prd_2')
elif etoos_ip in vpc_dev:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_dev')
elif etoos_ip in vpc_stg:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_stg')
elif etoos_ip in vpc_mgmt_prd:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_mgmt_prd')
elif etoos_ip in vpc_perf:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_perf')
elif etoos_ip in vpc_prd:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_prd')
elif etoos_ip in vpc_qa:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_qa')
elif etoos_ip in vpc_sand:
    print ('ETOOS-CPO-Platform-SEOUL / vpc_sand')
# ========
elif etoos_ip in edl_dev_vpc01:
    print ('ETOOS-aid-dev-SEOUL / edl_dev_vpc01')
# ========
elif etoos_ip in etoos_office_1:
    print ('ETOOS-office')
elif etoos_ip in etoos_office_2:
    print ('ETOOS-office')
elif etoos_ip in etoos_office_3:
    print ('ETOOS-office')
elif etoos_ip in etoos_office_4:
    print ('ETOOS-office')
