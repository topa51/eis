# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20160331_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='unixTimestamp',
            field=models.IntegerField(default=1459450134),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=models.IntegerField(default=1459450134),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.IntegerField(default=1459450134),
        ),
    ]
