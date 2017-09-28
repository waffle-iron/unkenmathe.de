# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0018_exercise_is_original'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='changes',
            field=models.CharField(choices=[('none', 'no changes')], default='none', max_length=15),
        ),
    ]