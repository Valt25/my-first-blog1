# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160526_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
    ]
