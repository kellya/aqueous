# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150602_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
