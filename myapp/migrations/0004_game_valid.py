# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]
