# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 20:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0009_answer_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='View360Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_upvotes', models.IntegerField(default=0)),
                ('nb_downvotes', models.IntegerField(default=0)),
                ('nb_views', models.IntegerField(default=0)),
                ('details', ckeditor_uploader.fields.RichTextUploadingField()),
                ('username', models.TextField()),
                ('anonymously', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'view_360_answer',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='anonymously',
            field=models.BooleanField(default=True),
        ),
    ]
