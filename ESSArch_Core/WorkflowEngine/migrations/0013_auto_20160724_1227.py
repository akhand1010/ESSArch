# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0012_auto_20160723_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processtask',
            name='started',
            field=models.DateTimeField(null=True, verbose_name='started at'),
        ),
    ]
