# Generated by Django 2.0.13 on 2019-04-07 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0030_auto_20190407_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='template',
            field=models.ForeignKey(limit_choices_to={'is_template': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tags.Structure', verbose_name='template'),
        ),
    ]