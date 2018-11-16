# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 11:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0005_department_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='header',
            field=models.CharField(default='', max_length=10, verbose_name='部门经理'),
        ),
        migrations.AddField(
            model_name='staff',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='入职时间'),
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hrm.Department', verbose_name='部门'),
        ),
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='部门名称'),
        ),
    ]
