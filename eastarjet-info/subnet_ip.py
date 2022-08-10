# 특정 IP 가 VPC CIDR 에 포함되면 무족건 검색
# 리전, 서브넷 대역 확인 시 사용되며 출력 내용을 수동으로 입력 하는 방식이라 주의사항 및 특이사항을 기재가능
import ipaddress

estar_ip = input('IP 를 넣어주세요 : ')

b_serial =[]
for i in ipaddress.IPv4Network('10.222.64.0/24'):
    ip_list = str(i)
    b_serial.append(ip_list)

b_serial_infor =[]
for i in ipaddress.IPv4Network('10.222.69.0/24'):
    ip_list = str(i)
    b_serial_infor.append(ip_list)

b_internal =[]
for i in ipaddress.IPv4Network('10.222.80.0/20'):
    ip_list = str(i)
    b_internal.append(ip_list)

b_dmz =[]
for i in ipaddress.IPv4Network('10.222.74.0/24'):
    ip_list = str(i)
    b_dmz.append(ip_list)

a_serial =[]
for i in ipaddress.IPv4Network('10.222.0.0/24'):
    ip_list = str(i)
    a_serial.append(ip_list)

a_internal_info =[]
for i in ipaddress.IPv4Network('10.222.5.0/24'):
    ip_list = str(i)
    a_internal_info.append(ip_list)

a_internal =[]
for i in ipaddress.IPv4Network('10.222.16.0/20'):
    ip_list = str(i)
    a_internal.append(ip_list)

a_dmzt =[]
for i in ipaddress.IPv4Network('10.222.15.0/24'):
    ip_list = str(i)
    a_dmzt.append(ip_list)

a_dmz =[]
for i in ipaddress.IPv4Network('10.222.10.0/24'):
    ip_list = str(i)
    a_dmz.append(ip_list)


if estar_ip in b_serial:
    print ('서울 / ZE_KOR_Subnet_B_Serial / ap-northeast-2c')
elif estar_ip in b_serial_infor:
    print ('서울 / ZE_KOR_Subnet_B_Internal_Info / ap-northeast-2c')
elif estar_ip in b_internal:
    print ('서울 / ZE_KOR_Subnet_B_Internal / ap-northeast-2c')
elif estar_ip in b_dmz:
    print ('서울 / ZE_KOR_Subnet_B_DMZ / ap-northeast-2c')
elif estar_ip in a_serial:
    print ('서울 / ZE_KOR_Subnet_A_Serial / ap-northeast-2a')
elif estar_ip in a_internal_info:
    print ('서울 / ZE_KOR_Subnet_A_Internal_Info / ap-northeast-2a')
elif estar_ip in a_internal:
    print ('서울 / ZE_KOR_Subnet_A_Internal / ap-northeast-2a')
elif estar_ip in a_dmzt:
    print ('서울 / ZE_KOR_Subnet_A_DMZT / ap-northeast-2a')
elif estar_ip in a_dmz:
    a = ('ap-northeast-2c')
    print (a)