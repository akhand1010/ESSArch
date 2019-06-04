# Generated by Django 2.0.13 on 2019-04-17 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0037_structuretype_editable_instance_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='noderelationtype',
            name='mirrored_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.NodeRelationType', verbose_name='mirrored type'),
        ),
    ]