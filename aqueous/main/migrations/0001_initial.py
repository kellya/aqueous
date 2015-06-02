# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('date_established', models.DateField()),
                ('volume', models.IntegerField()),
                ('notes', models.TextField()),
                ('type', models.IntegerField()),
            ],
        ),
    ]
