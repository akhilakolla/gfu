# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftsapp', '0004_auto_20170701_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('reviews', models.CharField(max_length=100)),
                ('imgpath', models.CharField(max_length=100)),
                ('imgname', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Occassion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occassion_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='gift_mapping',
            name='fgiftsid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftsapp.Gifts'),
        ),
        migrations.AddField(
            model_name='gift_mapping',
            name='focassid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftsapp.Occassion'),
        ),
    ]