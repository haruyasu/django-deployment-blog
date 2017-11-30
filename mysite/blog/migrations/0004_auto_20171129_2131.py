# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 05:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171129_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approve_comment',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 5, 31, 49, 538200, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 5, 31, 49, 538200, tzinfo=utc)),
        ),
    ]
