# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20180220_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_track',
            field=models.CharField(default='wait', max_length=13, verbose_name='Tracking'),
        ),
    ]