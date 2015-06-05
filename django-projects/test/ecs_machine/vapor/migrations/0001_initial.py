# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('InstanceId', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=20)),
                ('CreatedDate', models.DateField()),
                ('Owner', models.CharField(max_length=30)),
                ('OwnerId', models.CharField(max_length=20)),
                ('Account', models.CharField(max_length=30)),
                ('AccountId', models.CharField(max_length=20)),
                ('Group', models.CharField(max_length=30)),
                ('GroupId', models.CharField(max_length=20)),
                ('CostCenterId', models.CharField(max_length=20)),
                ('IsBackup', models.BooleanField(default=False)),
                ('IsLocked', models.BooleanField(default=False)),
                ('IsPatched', models.BooleanField(default=False)),
                ('IsLinux', models.BooleanField(default=False)),
                ('GpuEnabled', models.BooleanField(default=False)),
                ('Tag', models.TextField()),
                ('AdminGroup', models.CharField(max_length=30)),
                ('Description', models.TextField()),
                ('TerminateDate', models.DateField()),
                ('IpAddress', models.CharField(max_length=20)),
                ('RegionName', models.CharField(max_length=30)),
                ('RegionId', models.CharField(max_length=20)),
                ('ImageId', models.CharField(max_length=50)),
                ('ImageName', models.CharField(max_length=50)),
                ('Image', models.CharField(max_length=50)),
                ('OsVersion', models.CharField(max_length=20)),
                ('ServiceOfferingId', models.CharField(max_length=20)),
                ('ServiceOfferingName', models.CharField(max_length=30)),
                ('CpuNumber', models.IntegerField()),
                ('CpuSpeed', models.CharField(max_length=20)),
                ('Memory', models.CharField(max_length=20)),
                ('MemoryRaw', models.IntegerField()),
                ('CloudProviderName', models.CharField(max_length=50)),
                ('CloudProviderId', models.CharField(max_length=20)),
                ('OsTypeId', models.CharField(max_length=50)),
                ('Networks', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VolumeId', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=30)),
                ('Status', models.CharField(max_length=20)),
                ('CreatedDate', models.DateField()),
                ('Owner', models.CharField(max_length=30)),
                ('OwnerId', models.CharField(max_length=20)),
                ('Account', models.CharField(max_length=30)),
                ('AccountId', models.CharField(max_length=20)),
                ('Group', models.CharField(max_length=30)),
                ('GroupId', models.CharField(max_length=20)),
                ('CostCenterId', models.CharField(max_length=20)),
                ('Size', models.CharField(max_length=20)),
                ('RawSize', models.IntegerField()),
                ('Description', models.TextField()),
                ('Tag', models.TextField()),
                ('IsVisible', models.BooleanField(default=False)),
                ('Type', models.CharField(max_length=20)),
                ('Attached', models.BooleanField(default=False)),
                ('Instance', models.CharField(max_length=20)),
                ('InstanceId', models.CharField(max_length=50)),
                ('InstanceName', models.CharField(max_length=50)),
                ('InstanceState', models.CharField(max_length=20)),
                ('RegionId', models.CharField(max_length=20)),
                ('RegionName', models.CharField(max_length=30)),
                ('CloudProviderId', models.CharField(max_length=20)),
                ('CloudProviderName', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instance',
            name='Snapshots',
            field=models.ManyToManyField(to='vapor.Snapshot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='Volumes',
            field=models.ManyToManyField(to='vapor.Volume'),
            preserve_default=True,
        ),
    ]
