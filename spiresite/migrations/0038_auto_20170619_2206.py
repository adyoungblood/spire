# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 22:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0037_auto_20170619_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halloffamestandardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('two_columnn_block', wagtail.wagtailcore.blocks.StructBlock([(b'one', wagtail.wagtailcore.blocks.RichTextBlock()), (b'two', wagtail.wagtailcore.blocks.RichTextBlock())])), ('three_columnn_block', wagtail.wagtailcore.blocks.StructBlock([(b'one', wagtail.wagtailcore.blocks.RichTextBlock()), (b'two', wagtail.wagtailcore.blocks.RichTextBlock()), (b'three', wagtail.wagtailcore.blocks.RichTextBlock())]))]),
        ),
    ]