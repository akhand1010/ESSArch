# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-25 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0010_tagversion_reference_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='StructureUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('reference_code', models.CharField(max_length=255)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tags.StructureUnit')),
            ],
        ),
        migrations.AlterField(
            model_name='structure',
            name='version',
            field=models.CharField(default=b'1.0', max_length=255),
        ),
        migrations.AddField(
            model_name='structureunit',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='tags.Structure'),
        ),
        migrations.AlterUniqueTogether(
            name='structureunit',
            unique_together=set([('structure', 'reference_code')]),
        ),
    ]
