# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0008_staff_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='header',
            new_name='manager',
        ),
    ]
