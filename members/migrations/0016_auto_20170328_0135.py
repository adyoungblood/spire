# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 01:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_membereventpurchase_memberstatushistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='membership_expiration',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 1, 35, 53, 667013)),
        ),
        migrations.AddField(
            model_name='membershiplevel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
