# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170219_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.ImageField(upload_to='files'),
        ),
    ]
