# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部门名称')),
                ('number', models.IntegerField(verbose_name='部门人数')),
            ],
            options={
                'db_table': 'department_message',
                'verbose_name': '部门信息',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='员工姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('tel', models.CharField(max_length=20, verbose_name='手机号')),
            ],
            options={
                'db_table': 'staff_message',
                'verbose_name': '员工信息表',
            },
        ),
    ]
