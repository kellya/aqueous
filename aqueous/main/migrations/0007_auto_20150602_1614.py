# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150602_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='manufacturer',
            field=models.ForeignKey(blank=True, to='main.Manufacturer', null=True),
        ),
    ]
