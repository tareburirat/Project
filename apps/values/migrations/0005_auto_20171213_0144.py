# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0004_auto_20171212_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='properties_string',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
