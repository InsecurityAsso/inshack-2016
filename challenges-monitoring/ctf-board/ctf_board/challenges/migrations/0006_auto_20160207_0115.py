# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0005_auto_20160205_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='authors',
            field=models.CharField(max_length=50),
        ),
    ]
