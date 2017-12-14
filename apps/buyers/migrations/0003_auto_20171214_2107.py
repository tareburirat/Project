# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0002_auto_20171117_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
        ),
    ]
