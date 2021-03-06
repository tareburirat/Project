# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_status', models.IntegerField(choices=[(-2, 'Banned'), (-1, 'Expired'), (0, 'Draft'), (1, 'Sale'), (2, 'Booked'), (3, 'Sold')], default=0, verbose_name='Status')),
                ('date_of_sale', models.DateField(auto_now=True, verbose_name='Date of Sale')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('freight_fee', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Freight Fee')),
                ('freight', models.IntegerField(choices=[(0, 'Register'), (1, 'EMS'), (2, 'Kerry Express')], default=0, verbose_name='Freight')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('sequence', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Product')),
            ],
        ),
    ]
