# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pooopers', '0002_poooper_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poooper',
            name='salary',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
