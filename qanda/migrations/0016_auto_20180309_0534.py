# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import qanda.models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0015_auto_20180212_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_picture',
            field=models.ImageField(blank=True, null=True, upload_to=qanda.models.user_directory_path),
        ),
    ]
