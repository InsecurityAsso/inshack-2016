# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0007_challenge_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamflagchall',
            name='date_flagged',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]