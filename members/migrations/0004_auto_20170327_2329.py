# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20170327_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone_home',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_prefered',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
