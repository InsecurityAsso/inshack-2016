# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 17:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0007_auto_20160226_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamprofile',
            name='activation_key',
            field=models.CharField(default='default_key', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 14, 18, 12, 21, 585280)),
            preserve_default=False,
        ),
    ]
