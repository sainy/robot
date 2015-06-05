from django.db import models

# Create your models here.
class Snapshot(models.Model):
    pass


class Volume(models.Model):
    VolumeId = models.CharField(max_length=50)
    Name = models.CharField(max_length=30)
    Status =  models.CharField(max_length=20, default='Stopped')
    CreatedDate = models.DateTimeField('create date', blank=True, null=True)
    Owner = models.CharField(max_length=30)
    OwnerId = models.CharField(max_length=20)
    Account = models.CharField(max_length=30)
    AccountId =  models.CharField(max_length=20)
    Group = models.CharField(max_length=30)
    GroupId = models.CharField(max_length=20)
    CostCenterId = models.CharField(max_length=20)
    Size = models.CharField(max_length=20)
    RawSize = models.IntegerField(default=0)
    Description = models.TextField(default='-')
    Tag = models.TextField(default='-')
    IsVisible = models.BooleanField(default=False)
    Type = models.CharField(max_length=20)
    Attached = models.BooleanField(default=False)
    Instance = models.CharField(max_length=20)
    InstanceId = models.CharField(max_length=50)
    InstanceName = models.CharField(max_length=50)
    InstanceState = models.CharField(max_length=20)
    RegionId = models.CharField(max_length=20)
    RegionName = models.CharField(max_length=30)
    CloudProviderId = models.CharField(max_length=20)
    CloudProviderName = models.CharField(max_length=50)

    def __str__(self):
        return '\n'.join([self.Name, self.VolumeId])


class Instance(models.Model):
    InstanceId = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Status = models.CharField(max_length=20, default='Stopped')
    CreatedDate = models.DateTimeField('create date', blank=True, null=True)
    Owner = models.CharField(max_length=30)
    OwnerId = models.CharField(max_length=20)
    Account = models.CharField(max_length=30)
    AccountId = models.CharField(max_length=20)
    Group = models.CharField(max_length=30)
    GroupId = models.CharField(max_length=20)
    CostCenterId = models.CharField(max_length=20)
    IsBackup = models.BooleanField(default=False)
    IsLocked = models.BooleanField(default=False)
    IsPatched = models.BooleanField(default=False)
    IsLinux = models.BooleanField(default=False)
    GpuEnabled = models.BooleanField(default=False)
    Tag = models.TextField(default='-')
    AdminGroup = models.CharField(max_length=30, default="")
    Description = models.TextField(default='-')
    TerminateDate = models.DateTimeField('terminate data', blank=True, null=True)
    IpAddress = models.CharField(max_length=20)
    RegionName = models.CharField(max_length=30)
    RegionId = models.CharField(max_length=20)
    ImageId = models.CharField(max_length=50)
    ImageName = models.CharField(max_length=50)
    Image = models.CharField(max_length=50, default="")
    OsVersion = models.CharField(max_length=20)
    ServiceOfferingId = models.CharField(max_length=20)
    ServiceOfferingName = models.CharField(max_length=30)
    CpuNumber = models.IntegerField(default=1)
    CpuSpeed = models.CharField(max_length=20)
    Memory = models.CharField(max_length=20)
    MemoryRaw = models.IntegerField(default=0)
    CloudProviderName = models.CharField(max_length=50)
    CloudProviderId = models.CharField(max_length=20)
    OsTypeId = models.CharField(max_length=50)
    Volumes = models.ManyToManyField(Volume)
    Snapshots = models.ManyToManyField(Snapshot)
    Networks = models.CharField(max_length=30)

    def __str__(self):
        return '\n'.join([self.Name, self.InstanceId])

