# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-15 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='key',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='key',
            field=models.IntegerField(),
        ),
    ]
