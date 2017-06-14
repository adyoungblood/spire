# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_membershiplevel_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membershiplevel',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membershiplevel',
            name='slug',
        ),
        migrations.AddField(
            model_name='membershiplevel',
            name='access_level',
            field=models.IntegerField(default=0, help_text='0: guest ( No Access to member areas), Above a 0 is considered a full member'),
        ),
    ]
