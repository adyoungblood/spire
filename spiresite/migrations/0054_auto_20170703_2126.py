# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 21:26
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0053_auto_20170629_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.URLBlock()), (b'label', wagtail.wagtailcore.blocks.CharBlock())])), ('people_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(null=True)), (b'name', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock())]), icon='group', template='spiresite/blocks/people_list.html')), ('redirect', wagtail.wagtailcore.blocks.StructBlock([(b'page', wagtail.wagtailcore.blocks.PageChooserBlock())])), ('REAL_page', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'event', wagtail.wagtailcore.blocks.RichTextBlock())]))]),
        ),
    ]