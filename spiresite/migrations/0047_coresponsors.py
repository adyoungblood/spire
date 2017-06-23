# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('spiresite', '0046_auto_20170622_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreSponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sponsor_logo', to='wagtailimages.Image')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_sponsors', to='spiresite.ThemeSettings')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]