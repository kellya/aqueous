# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='tank',
            name='type',
            field=models.ForeignKey(to='main.Type'),
        ),
    ]
