# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftsapp', '0008_auto_20170705_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(max_length=2),
        ),
    ]