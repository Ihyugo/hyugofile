# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170222_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='photofile',
            new_name='file',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='name',
        ),
    ]
