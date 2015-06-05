# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapor', '0002_auto_20150320_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='CreatedDate',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='TerminateDate',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volume',
            name='CreatedDate',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
