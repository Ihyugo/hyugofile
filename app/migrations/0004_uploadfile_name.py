# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170222_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='name',
            field=models.CharField(default='DUMMY', max_length=40),
            preserve_default=False,
        ),
    ]
