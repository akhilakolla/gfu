# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftsapp', '0006_auto_20170703_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gifts',
            name='imgpath',
            field=models.CharField(max_length=200),
        ),
    ]
