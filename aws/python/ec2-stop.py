import boto3
region = 'eu-central-1'
ec2 = boto3.client('ec2', region_name='eu-west-1')
response = ec2.describe_instances(Filters=[
        {
            'Name': 'tag:Environment',
            'Values': [
                'awslab',
            ]
        },
    ])

instances = []

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instances.append(instance["InstanceId"])

ec2.stop_instances(InstanceIds=instances)
print('stopped instances: ' + str(instances))