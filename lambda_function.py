import boto3
import json

def stop_task_handler(event, context):
    if event.get('cluster_name') is None:
        raise NameError("cluster_name does not set")

    if event.get('service_name') is None:
        raise NameError("service_name does not set")

    ecs_client = boto3.client("ecs", region_name="ap-northeast-1")
    tasks = ecs_client.list_tasks(cluster=event.get('cluster_name'), serviceName=event.get('service_name'))
    
    for task_arn in tasks['taskArns']:
        ecs_client.stop_task(cluster=event.get('cluster_name'), task=task_arn)

def restart_service_handler(event, context):
    force_restart = False

    if event.get('cluster_name') is None:
        raise NameError("cluster_name does not set")

    if event.get('service_name') is None:
        raise NameError("service_name does not set")
    
    if event.get('force_restart') is not None:
        force_restart = json.load(event.get('force_restart'))

    ecs_client = boto3.client("ecs", region_name="ap-northeast-1")
    ecs_client.update_service(cluster=event.get('cluster_name'), serviceName=event.get('service_name'), forceNewDeployment=force_restart)

def _validate_event_arguments(event):

if __name__ == '__main__':
    event = {
        'cluster_name': 'rodgers-cluster',
        'service_name': 'rodgers-service'
    }
    context = {}
    stop_task_handler(event, context)
