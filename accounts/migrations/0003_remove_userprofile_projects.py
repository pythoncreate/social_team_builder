# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-17 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170717_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='projects',
        ),
    ]