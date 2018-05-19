import boto3
import  datetime

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


for instance in instances:
    all_amis = []

    instance_id = instance.id
    print("Instance Type: " + instance.instance_type)

    #Getting Instance Name
    instance_tags = instance.tags
    name_tag = instance_tags[0]
    instance_name = name_tag['Value']

    create_time = datetime.datetime.now()
    create_fmt = create_time.strftime('%Y-%m-%d')

    ami_id = client.create_image(InstanceId=instance_id, Name= instance_name+'-'+instance_id+'-'+create_fmt, NoReboot=True, DryRun=False)

    all_amis.append(ami_id['ImageId'])

    client.create_tags(
        Resources=all_amis,
        Tags=[
            {'Key': 'Name', 'Value': instance_name}
        ]
    )