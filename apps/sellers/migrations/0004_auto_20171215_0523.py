# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_auto_20171214_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='expire_date',
            field=models.IntegerField(default=0, verbose_name='Expiredate'),
        ),
    ]