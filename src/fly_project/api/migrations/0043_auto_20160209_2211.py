# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 22:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_notification_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='text',
            new_name='description',
        ),
    ]