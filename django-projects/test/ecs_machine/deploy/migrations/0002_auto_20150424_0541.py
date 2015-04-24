# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployInstanceShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance', models.ForeignKey(to='deploy.Instances')),
                ('sheet', models.ForeignKey(to='deploy.DeploySheet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeployVariableShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sheet', models.ForeignKey(to='deploy.DeploySheet')),
                ('variable', models.ForeignKey(to='deploy.Variables')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='deployship',
            name='instance',
        ),
        migrations.RemoveField(
            model_name='deployship',
            name='variable',
        ),
        migrations.AlterField(
            model_name='deploysheet',
            name='instances',
            field=models.ManyToManyField(to='deploy.Instances', through='deploy.DeployInstanceShip'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deploysheet',
            name='varibles',
            field=models.ManyToManyField(to='deploy.Variables', through='deploy.DeployVariableShip'),
            preserve_default=True,
        ),
    ]
