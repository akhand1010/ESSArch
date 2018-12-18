"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Core
    Copyright (C) 2005-2017 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 15:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def forwards_func(apps, schema_editor):
    IP = apps.get_model("ip", "InformationPackage")
    Event = apps.get_model("ip", "EventIP")
    User = apps.get_model("auth", "User")
    db_alias = schema_editor.connection.alias

    ips = IP.objects.using(db_alias).all()
    events = Event.objects.using(db_alias).all()

    for ip in ips:
        try:
            ip.Responsible = str(User.objects.using(db_alias).get(username=ip.Responsible).id)
            ip.save()
        except:
            pass

    for event in events:
        try:
            event.linkingAgentIdentifierValue = str(User.objects.using(db_alias).get(username=event.linkingAgentIdentifierValue).id)
            event.save()
        except:
            pass


def reverse_func(apps, schema_editor):
    IP = apps.get_model("ip", "InformationPackage")
    Event = apps.get_model("ip", "EventIP")
    User = apps.get_model("auth", "User")
    db_alias = schema_editor.connection.alias

    ips = IP.objects.using(db_alias).all()
    events = Event.objects.using(db_alias).all()

    for ip in ips:
        try:
            ip.Responsible = str(User.objects.using(db_alias).get(pk=ip.Responsible).username)
            ip.save()
        except:
            pass

    for event in events:
        try:
            event.linkingAgentIdentifierValue = str(User.objects.using(db_alias).get(pk=event.linkingAgentIdentifierValue).username)
            event.save()
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0022_auto_20161205_2226'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
        migrations.AlterField(
            model_name='eventip',
            name='linkingAgentIdentifierValue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='informationpackage',
            name='Responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='information_packages', to=settings.AUTH_USER_MODEL),
        ),
    ]