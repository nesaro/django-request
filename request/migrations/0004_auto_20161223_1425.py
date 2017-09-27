# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_remove_request_get_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='ip address'),
        ),
        migrations.AlterField(
            model_name='request',
            name='method',
            field=models.CharField(default='GET', max_length=7, verbose_name='method'),
        ),
        migrations.AlterField(
            model_name='request',
            name='time',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='time'),
        ),
    ]