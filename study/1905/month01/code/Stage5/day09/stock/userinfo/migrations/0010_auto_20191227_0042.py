# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-26 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0009_auto_20191226_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
    ]
