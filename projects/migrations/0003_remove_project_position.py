# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-17 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170717_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='position',
        ),
    ]