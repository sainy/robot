# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapor', '0003_auto_20150320_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='CpuNumber',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='MemoryRaw',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volume',
            name='RawSize',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
