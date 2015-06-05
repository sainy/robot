# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapor', '0004_auto_20150320_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='TerminateDate',
            field=models.DateTimeField(verbose_name=b'date terminate'),
            preserve_default=True,
        ),
    ]
