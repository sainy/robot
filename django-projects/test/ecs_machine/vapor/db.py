from models import Instance
from django.utils import timezone

def createInstance(InsDict):
    instance = Instance(InstanceId=InsDict['InstanceId'], Name=InsDict['Name'], CreatedDate=InsDict['CreatedDate'], Owner=InsDict['Owner'],
                        OwnerId=InsDict['OwnerId'], Account=InsDict['Account'], AccountId=InsDict['AccountId'], Group=InsDict['Group'], GroupId=InsDict['GroupId'],
                        CostCenterId=InsDict['CostCenterId'], IpAddress=InsDict['IpAddress'], RegionName=InsDict['RegionName'],
                        RegionId=InsDict['RegionId'], ImageId=InsDict['ImageId'], ImageName=InsDict['ImageName'], OsVersion=InsDict['OsVersion'], CpuNumber=InsDict['CpuNumber'],
                        CpuSpeed=InsDict['CpuSpeed'], ServiceOfferingId=InsDict['ServiceOfferingId'], ServiceOfferingName=InsDict['ServiceOfferingName'], Memory=InsDict['Memory'],
                        MemoryRaw=InsDict['MemoryRaw'], CloudProviderName=InsDict['CloudProviderName'], CloudProviderId=InsDict['CloudProviderId'], OsTypeId=InsDict['OsTypeId'])
    instance.save()

def deleteInstance(instance):
    instance.delete()

def queryInstancebyId(instanceid):
    return Instance.objects.filter(InstanceId=instanceid).exists()

def getInstancebyName(name):
    return Instance.objects.filter(Name=name)

def getInstancebyStatus(status):
    return Instance.objects.filter(Status=status)

def getInstancebyOwner(owner):
    return Instance.objects.filter(Owner=owner)

def getInstancebyGroup(group):
    return Instance.objects.filter(Group=group)

def getAllInstance():
    return Instance.objects.all()
    
    
