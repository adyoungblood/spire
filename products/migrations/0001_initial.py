# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0003_memberprofesionalinformation_title'),
        ('events', '0003_event_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_product', to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('membership_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_product', to='members.MembershipLevel')),
            ],
        ),
    ]
