# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='summary',
        ),
        migrations.AddField(
            model_name='movie',
            name='ranking',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
