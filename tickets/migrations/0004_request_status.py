# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20160111_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Cancelled'), ('S', 'Standard'), ('Q', 'Queue Jump'), ('D', 'Dining')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]
