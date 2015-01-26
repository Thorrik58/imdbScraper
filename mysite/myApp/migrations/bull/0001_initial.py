# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('rating', models.FloatField(default=0.0)),
                ('year', models.IntegerField(default=0)),
                ('summary', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
