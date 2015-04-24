from django.db import models

class Variables(models.Model):
    Attr_Name = models.CharField(max_length=50)
    Attr_Value = models.CharField(max_length=200)

    def __str__(self):
        return self.Attr_Name


class Instances(models.Model):
    Instance = models.CharField(max_length=50)
    Inst_Name = models.CharField(max_length=50)
    Inst_Id = models.CharField(max_length=50)
    Inst_Ip = models.CharField(max_length=20)
    Inst_Fqdn = models.CharField(max_length=50)
    Inst_Cmd = models.CharField(max_length=200)

    def __str__(self):
        return self.Inst_Name

class Deploys(models.Model):
    Instance = models.ForeignKey(Instances)
    Order = models.IntegerField(default=3)
    Cmd = models.CharField(max_length=200)
    Status = models.IntegerField(default=1)

    def __str__(self):
        return self.Instance

class DeploySheet(models.Model):
    name = models.CharField(max_length=50, default="")
    varibles = models.ManyToManyField(Variables, through='DeployVariableShip')
    instances = models.ManyToManyField(Instances, through='DeployInstanceShip')
    deploys = models.ManyToManyField(Deploys, through='DeployShip')

    def __str__(self):
        return self.name

class DeployInstanceShip(models.Model):
    instance = models.ForeignKey(Instances)
    sheet = models.ForeignKey(DeploySheet)

class DeployVariableShip(models.Model):
    variable = models.ForeignKey(Variables)
    sheet = models.ForeignKey(DeploySheet)

class DeployShip(models.Model):
    deploy = models.ForeignKey(Deploys)
    sheet = models.ForeignKey(DeploySheet)

# Create your models here.
