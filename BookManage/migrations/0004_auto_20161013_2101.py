# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookManage', '0003_auto_20161013_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='AuthorID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]