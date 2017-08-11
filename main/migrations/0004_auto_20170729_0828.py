# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170728_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='protocol',
        ),
        migrations.RemoveField(
            model_name='modbus',
            name='id',
        ),
        migrations.AddField(
            model_name='modbus',
            name='device_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Device'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='Название'),
        ),
    ]
