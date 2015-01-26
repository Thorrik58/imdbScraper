# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20150126_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='pubdate',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='ranking',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
