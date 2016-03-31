# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160331_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='unixTimestamp',
            field=models.DecimalField(decimal_places=10, max_digits=65, default=1459448950.784521),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=models.IntegerField(default=1459448950),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.IntegerField(default=1459448950),
        ),
    ]
