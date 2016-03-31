# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160331_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='unixTimestamp',
            field=models.DecimalField(default=1459448598.13792, decimal_places=10, max_digits=65),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=models.DecimalField(default=1459448598.138386, decimal_places=10, max_digits=65),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.DecimalField(default=1459448598.137239, decimal_places=10, max_digits=65),
        ),
    ]
