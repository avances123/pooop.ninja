# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pooop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField()),
                ('poooper', models.ForeignKey(related_name='pooops', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['end'],
            },
        ),
    ]
