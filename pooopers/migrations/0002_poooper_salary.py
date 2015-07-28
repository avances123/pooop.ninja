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
            name='salary',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=24),
        ),
    ]
