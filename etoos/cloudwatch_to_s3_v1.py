import boto3
import os
from pprint import pprint
import time
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta

logs = boto3.client('logs')

def lambda_handler(event, context):
    extra_args = {}
    log_groups = []
    log_groups_to_export = []
    
    if 'platform-prd-logs' not in os.environ:
        print("Error: platform-prd-logs not defined")
        return
    
    print("--> platform-prd-logs=%s" % os.environ["platform-prd-logs"])
    
    while True:
        response = logs.describe_log_groups(**extra_args)
        log_groups = log_groups + response['logGroups']
        
        if not 'nextToken' in response:
            break
        extra_args['nextToken'] = response['nextToken']
    
    for log_group in log_groups:
        response = logs.list_tags_log_group(logGroupName=log_group['logGroupName'])
        log_group_tags = response['tags']
        if 'ExportToS3' in log_group_tags and log_group_tags['ExportToS3'] == '1':
            log_groups_to_export.append(log_group['logGroupName'])
        time.sleep(1)
            
    
    for log_group_name in log_groups_to_export:
        first_day = datetime.today() - relativedelta(months=1)
        last_day = datetime.today()
        froms = int(first_day.timestamp() * 1000)
        tos = int(last_day.timestamp()*1000)
        
        try:
            response = logs.create_export_task(
                logGroupName=log_group_name,
                fromTime=froms,
                to=tos,
                destination=os.environ['platform-prd-logs'],
                destinationPrefix=os.path.join('cloudwatch', log_group_name.strip('/').replace('/','_'), first_day.strftime('%Y-%m-').format(os.path.sep))
            )
            print("    Task created: %s" % response['taskId'])
            time.sleep(1)
            
        except logs.exceptions.LimitExceededException:
            print("    Need to wait until all tasks are finished (LimitExceededException). Continuing later...")
            return
        
        except Exception as e:
            print("    Error exporting %s: %s" % (log_group_name, getattr(e, 'message', repr(e))))
            continue