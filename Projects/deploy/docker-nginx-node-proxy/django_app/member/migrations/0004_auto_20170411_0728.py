# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 07:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20170411_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerytest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 11, 7, 28, 4, 306792, tzinfo=utc)),
        ),
    ]
