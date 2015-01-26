# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20150126_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
    ]
