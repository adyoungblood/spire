# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('events', '0002_auto_20170613_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('can_attend', models.BooleanField(default=False)),
                ('event_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_pricings', to='events.Event')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_level', to='members.MembershipLevel')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
