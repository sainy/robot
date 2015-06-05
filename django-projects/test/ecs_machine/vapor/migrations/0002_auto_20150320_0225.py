# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='TerminateDate',
            field=models.DateField(default=None),
            preserve_default=True,
        ),
    ]
