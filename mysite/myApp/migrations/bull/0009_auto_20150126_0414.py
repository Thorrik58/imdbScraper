# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20150126_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
