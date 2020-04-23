# Generated by Django 3.0.3 on 2020-03-09 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
        ('configuration', '0023_auto_20200211_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagepolicy',
            name='cache_storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cache_policy', to='storage.StorageMethod'),
        ),
    ]
