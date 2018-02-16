# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180128_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Product Summary',
                'proxy': True,
                'indexes': [],
                'verbose_name_plural': 'Products Summary',
            },
            bases=('products.product',),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_sale',
            field=models.DateTimeField(auto_now=True, verbose_name='Date of Sale'),
        ),
    ]