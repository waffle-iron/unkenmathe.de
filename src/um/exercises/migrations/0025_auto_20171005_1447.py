# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0024_exercise_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='license',
            field=models.CharField(choices=[('cc-by', 'CC BY 4.0'), ('cc-by-sa', 'CC BY-SA 4.0')], default='cc-by', max_length=15),
        ),
    ]
