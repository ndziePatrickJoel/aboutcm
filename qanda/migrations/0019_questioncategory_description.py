# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0018_auto_20180314_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioncategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]