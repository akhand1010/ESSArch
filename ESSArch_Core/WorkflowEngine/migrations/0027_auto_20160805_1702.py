# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0026_auto_20160805_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processtask',
            name='attempt',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='processtask',
            name='processstep_pos',
            field=models.IntegerField(default=0, verbose_name='ProcessStep position'),
        ),
        migrations.AlterField(
            model_name='processtask',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
