# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 21:47
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0002_remove_homepage_hero_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sponsor_one',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sponsor_three',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sponsor_two',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
