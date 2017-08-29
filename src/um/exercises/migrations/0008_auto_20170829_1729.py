# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_auto_20170828_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='created',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='modified',
        ),
        migrations.AddField(
            model_name='exercise',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]
