# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161021_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.CharField(default=None, max_length=200),
        ),
    ]