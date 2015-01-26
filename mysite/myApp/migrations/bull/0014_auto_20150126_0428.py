# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_auto_20150126_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pubdate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
