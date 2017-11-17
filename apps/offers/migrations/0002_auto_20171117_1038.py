# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Offer Price'),
        ),
    ]
