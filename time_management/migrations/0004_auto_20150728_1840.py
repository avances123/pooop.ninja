# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_management', '0003_auto_20150728_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pooop',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
