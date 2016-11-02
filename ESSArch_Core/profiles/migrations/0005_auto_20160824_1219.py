# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20160824_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_aip',
            field=models.ManyToManyField(through='profiles.ProfileAIPRel', to='profiles.ProfileAIP'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_classification',
            field=models.ManyToManyField(through='profiles.ProfileClassificationRel', to='profiles.ProfileClassification'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_content_type',
            field=models.ManyToManyField(through='profiles.ProfileContentTypeRel', to='profiles.ProfileContentType'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_data_selection',
            field=models.ManyToManyField(through='profiles.ProfileDataSelectionRel', to='profiles.ProfileDataSelection'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_dip',
            field=models.ManyToManyField(through='profiles.ProfileDIPRel', to='profiles.ProfileDIP'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_import',
            field=models.ManyToManyField(through='profiles.ProfileImportRel', to='profiles.ProfileImport'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_preservation_metadata',
            field=models.ManyToManyField(through='profiles.ProfilePreservationMetadataRel', to='profiles.ProfilePreservationMetadata'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_sip',
            field=models.ManyToManyField(through='profiles.ProfileSIPRel', to='profiles.ProfileSIP'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_submit_description',
            field=models.ManyToManyField(through='profiles.ProfileSubmitDescriptionRel', to='profiles.ProfileSubmitDescription'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_transfer_project',
            field=models.ManyToManyField(through='profiles.ProfileTransferProjectRel', to='profiles.ProfileTransferProject'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_workflow',
            field=models.ManyToManyField(through='profiles.ProfileWorkflowRel', to='profiles.ProfileWorkflow'),
        ),
    ]
