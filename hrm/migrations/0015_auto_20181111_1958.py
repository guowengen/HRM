# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-11 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0014_auto_20181111_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]