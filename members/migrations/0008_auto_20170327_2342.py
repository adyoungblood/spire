# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20170327_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='/home/douglas/dev/repos/spire/spire/media/defaults/headshot.png', upload_to='/home/douglas/dev/repos/spire/spire/media/members'),
        ),
    ]
