# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20161121_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengeprogress',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='progress',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
