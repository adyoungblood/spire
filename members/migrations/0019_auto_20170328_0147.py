# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 01:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_auto_20170328_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership_expiration',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 1, 47, 42, 368300)),
        ),
    ]
