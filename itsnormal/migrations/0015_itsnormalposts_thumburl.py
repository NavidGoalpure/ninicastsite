# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsnormal', '0014_remove_itsnormalposts_thumburl'),
    ]

    operations = [
        migrations.AddField(
            model_name='itsnormalposts',
            name='thumbUrl',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
