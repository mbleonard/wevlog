# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(default='no job', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='user without description'),
        ),
    ]
