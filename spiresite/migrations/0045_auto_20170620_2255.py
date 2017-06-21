# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 22:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spiresite', '0044_job_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='slug',
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='organization',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]