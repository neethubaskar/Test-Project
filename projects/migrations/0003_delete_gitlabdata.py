# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-12 03:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_gitlabdata_vchr_pin_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GitlabData',
        ),
    ]