# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pubdate',
            field=models.DateField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
    ]
