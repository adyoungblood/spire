# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_membershiplevel_slug'),
        ('spiresite', '0015_srecmemberspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='srecmemberspage',
            name='srec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='srec_membership_level', to='members.MembershipLevel'),
        ),
    ]