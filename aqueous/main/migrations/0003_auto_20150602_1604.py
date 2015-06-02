# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150602_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=32)),
                ('webpage', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='tank',
            name='manufacturer',
            field=models.ForeignKey(to='main.Manufacturer', null=True),
        ),
    ]
