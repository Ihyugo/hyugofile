# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170305_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]