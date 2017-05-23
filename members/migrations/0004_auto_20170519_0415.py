# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-19 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_memberaddress_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProffesionalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_one', models.CharField(max_length=255)),
                ('address_line_two', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('assistant_name', models.CharField(blank=True, max_length=255)),
                ('assistant_email', models.EmailField(blank=True, max_length=255)),
                ('assistant_phone', models.CharField(blank=True, max_length=255)),
                ('company', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='company',
        ),
        migrations.AddField(
            model_name='member',
            name='preffered_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]