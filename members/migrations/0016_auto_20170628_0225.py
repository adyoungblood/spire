# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_auto_20170627_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membertag',
            name='tag',
            field=models.SlugField(max_length=255),
        ),
    ]
