# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150602_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='phone',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='webpage',
            field=models.URLField(null=True, blank=True),
        ),
    ]
