# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_remove_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 1, 26, 4, 13, 26, 970416, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
