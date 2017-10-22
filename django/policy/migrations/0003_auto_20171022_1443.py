# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0002_auto_20171022_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentinfo',
            options={'verbose_name': 'payment information'},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name': 'application stage'},
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='name',
            new_name='current_stage',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='start_time',
        ),
    ]
