# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_membershiplevel_expires'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='skills_specialties',
        ),
    ]
