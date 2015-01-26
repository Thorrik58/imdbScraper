# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_auto_20150126_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pubdate',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
