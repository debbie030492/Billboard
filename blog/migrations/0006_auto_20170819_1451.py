# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-19 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170819_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=80, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='empty title', max_length=100, null=True),
        ),
    ]
