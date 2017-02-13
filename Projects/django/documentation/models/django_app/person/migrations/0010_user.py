# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20170209_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('followers', models.ManyToManyField(related_name='_user_followers_+', to='person.User')),
                ('following', models.ManyToManyField(related_name='_user_following_+', to='person.User')),
            ],
        ),
    ]