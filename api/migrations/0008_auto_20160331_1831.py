# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160331_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='unixTimestamp',
            field=models.DecimalField(default=1459449062.28528, decimal_places=10, max_digits=65),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=models.DecimalField(default=1459449062.285749, decimal_places=10, max_digits=65),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.DecimalField(default=1459449062.284466, decimal_places=10, max_digits=65),
        ),
    ]
