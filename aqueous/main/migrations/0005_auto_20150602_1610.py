# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150602_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
