import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    #Getting Instance Name
    instance_tags = instance.tags
    name_tag = instance_tags[0]
    instance_name = name_tag['Value']

    print("--------------------")
    print("Instance Name: " + instance_name)
    print("Instance Id: " + instance.id)
    print("Instance Type: " + instance.instance_type)