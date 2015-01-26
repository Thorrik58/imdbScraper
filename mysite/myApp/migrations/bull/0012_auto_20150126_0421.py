# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_auto_20150126_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 1, 26, 4, 21, 43, 142584, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='pubdate',
            field=models.DateField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='ranking',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
