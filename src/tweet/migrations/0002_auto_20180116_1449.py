# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-16 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='content1',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='content3',
        ),
    ]