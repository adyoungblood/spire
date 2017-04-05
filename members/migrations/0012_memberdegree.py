# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20170328_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('UNDERGRAD', 'Undergraduate'), ('MA', 'MA'), ('MS', 'MS'), ('MBA', 'MBA'), ('JD', 'JD'), ('PHD', 'PHD')], max_length=50)),
                ('grad_year', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
        ),
    ]
