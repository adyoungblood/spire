# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_membershipproduct_subscription'),
        ('spiresite', '0027_auto_20170531_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershippage',
            name='full_friends_yearly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_full_friends', to='products.MembershipProduct'),
        ),
        migrations.AddField(
            model_name='membershippage',
            name='full_young_yearly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_full_young', to='products.MembershipProduct'),
        ),
        migrations.AddField(
            model_name='membershippage',
            name='guest_yearly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_guest', to='products.MembershipProduct'),
        ),
        migrations.AddField(
            model_name='membershippage',
            name='student_yearly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_student', to='products.MembershipProduct'),
        ),
    ]