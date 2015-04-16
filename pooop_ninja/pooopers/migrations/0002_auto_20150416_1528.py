# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pooopers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poooper',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='poooper',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poooper',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
