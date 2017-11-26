# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_assigned_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.School'),
        ),
    ]