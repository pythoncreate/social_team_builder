# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-17 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='position',
            field=models.ForeignKey(default='engineer', on_delete=django.db.models.deletion.CASCADE, to='projects.Position'),
        ),
        migrations.AlterField(
            model_name='project',
            name='skill',
            field=models.ForeignKey(default='java', on_delete=django.db.models.deletion.CASCADE, to='projects.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('1', 'Android Developer'), ('2', 'Designer'), ('3', 'Java Developer'), ('4', 'PHP Developer'), ('5', 'Python Developer'), ('6', 'Rails Developer'), ('7', 'Wordpress Developer'), ('8', 'iOS Developer')], default='unknown', max_length=140),
        ),
    ]