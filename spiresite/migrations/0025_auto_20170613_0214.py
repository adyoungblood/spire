# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0024_jobpage_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpricing',
            name='ticket_quantity',
        ),
        migrations.AddField(
            model_name='eventpricing',
            name='can_attend',
            field=models.BooleanField(default=False),
        ),
    ]
