# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giftsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_pwd_reset',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_self_rating',
        ),
    ]
