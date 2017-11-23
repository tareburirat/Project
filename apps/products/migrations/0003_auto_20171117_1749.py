# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171117_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('sequence', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='freight_detail_choices',
        ),
        migrations.AddField(
            model_name='product',
            name='freight_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Freight Fee'),
        ),
        migrations.AlterField(
            model_name='product',
            name='freight',
            field=models.IntegerField(choices=[(0, 'Register'), (1, 'EMS'), (2, 'Kerry Express')], default=0, verbose_name='Freight'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Product'),
        ),
    ]
