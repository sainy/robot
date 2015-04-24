# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapor', '0005_auto_20150320_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='CreatedDate',
            field=models.DateTimeField(null=True, verbose_name=b'create date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='Description',
            field=models.TextField(default=b'-'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='Image',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='Status',
            field=models.CharField(default=b'Stopped', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='Tag',
            field=models.TextField(default=b'-'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='TerminateDate',
            field=models.DateTimeField(null=True, verbose_name=b'terminate data', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volume',
            name='CreatedDate',
            field=models.DateTimeField(null=True, verbose_name=b'create date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volume',
            name='Description',
            field=models.TextField(default=b'-'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volume',
            name='Status',
            field=models.CharField(default=b'Stopped', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volume',
            name='Tag',
            field=models.TextField(default=b'-'),
            preserve_default=True,
        ),
    ]
