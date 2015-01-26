# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_auto_20150126_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pubdate',
            field=models.DateField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
