# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0005_auto_20170529_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact_content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_link',
            field=models.URLField(blank=True),
        ),
    ]
