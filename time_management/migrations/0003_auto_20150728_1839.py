# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_management', '0002_auto_20150629_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pooop',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
    ]
