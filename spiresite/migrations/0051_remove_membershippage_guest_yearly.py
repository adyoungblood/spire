# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0050_resumebookpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membershippage',
            name='guest_yearly',
        ),
    ]
