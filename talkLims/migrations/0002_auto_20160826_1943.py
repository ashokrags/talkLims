# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-26 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('talkLims', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestinfo',
            old_name='number_read',
            new_name='number_of_reads',
        ),
        migrations.RenameField(
            model_name='requestinfo',
            old_name='number_samples',
            new_name='number_of_samples',
        ),
    ]
