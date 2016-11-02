# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0035_auto_20160819_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='steptask',
            name='step',
        ),
        migrations.RemoveField(
            model_name='steptask',
            name='task',
        ),
        migrations.DeleteModel(
            name='Step',
        ),
        migrations.DeleteModel(
            name='StepTask',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
