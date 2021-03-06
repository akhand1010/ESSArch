# Generated by Django 3.1.2 on 2020-10-26 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0071_merge_20201025_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendering',
            name='custom_fields',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='rendering',
            name='file',
            field=models.FileField(upload_to='stylesheets/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xslt'])]),
        ),
    ]
