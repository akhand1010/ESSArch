# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('agentType', models.CharField(max_length=60, unique=True)),
                ('agentDetail', models.CharField(max_length=70)),
            ],
            options={
                'ordering': ['agentType'],
                'verbose_name': 'Agent',
            },
        ),
    ]
