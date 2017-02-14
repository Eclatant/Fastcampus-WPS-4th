# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='유저네임')),
                ('last_name', models.CharField(max_length=20, verbose_name='성')),
                ('first_name', models.CharField(max_length=20, verbose_name='이름')),
                ('nickname', models.CharField(max_length=24, verbose_name='닉네임')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='이메일')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('following', models.ManyToManyField(blank=True, to='member.MyUser')),
            ],
        ),
    ]