# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-27 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterLike',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('access_token', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
            ],
        ),
    ]
