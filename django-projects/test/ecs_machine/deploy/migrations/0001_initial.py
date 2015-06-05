# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deploys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Order', models.IntegerField(default=3)),
                ('Cmd', models.CharField(max_length=200)),
                ('Status', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploySheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instances',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Instance', models.CharField(max_length=50)),
                ('Inst_Name', models.CharField(max_length=50)),
                ('Inst_Id', models.CharField(max_length=50)),
                ('Inst_Ip', models.CharField(max_length=20)),
                ('Inst_Fqdn', models.CharField(max_length=50)),
                ('Inst_Cmd', models.CharField(max_length=200)),
                ('sheet', models.ForeignKey(to='deploy.DeploySheet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Attr_Name', models.CharField(max_length=50)),
                ('Attr_Value', models.CharField(max_length=200)),
                ('sheet', models.ForeignKey(to='deploy.DeploySheet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deploys',
            name='Instance',
            field=models.ForeignKey(to='deploy.Instances'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deploys',
            name='sheet',
            field=models.ForeignKey(to='deploy.DeploySheet'),
            preserve_default=True,
        ),
    ]
