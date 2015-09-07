# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('time_management', '0004_auto_20150728_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pooop',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
