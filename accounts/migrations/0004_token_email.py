# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
