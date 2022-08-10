import boto3
import pprint

client = boto3.client('ec2', region_name='ap-southeast-2')
volume = client.describe_volumes()
pprint.pprint (volume)
# volume = volume['Volumes']
# for i in volume[0:]:
#     volume_Size = i
#     volume_Size = volume_Size['Size']
#     pprint.pprint (volume_Size)

