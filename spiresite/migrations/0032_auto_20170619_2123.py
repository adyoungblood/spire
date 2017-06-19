# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 21:23
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0031_annualreports_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('button', wagtail.wagtailcore.blocks.StreamBlock([(b'link', wagtail.wagtailcore.blocks.URLBlock())]))]),
        ),
    ]
