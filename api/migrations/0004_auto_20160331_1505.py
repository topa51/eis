# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160331_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='unixTimestamp',
            field=models.IntegerField(default=1459436735),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='lat',
            field=models.DecimalField(max_digits=65, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='lng',
            field=models.DecimalField(max_digits=65, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=models.IntegerField(default=1459436735),
        ),
        migrations.AlterField(
            model_name='ship',
            name='lat',
            field=models.DecimalField(max_digits=65, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='ship',
            name='lng',
            field=models.DecimalField(max_digits=65, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.IntegerField(default=1459436735),
        ),
    ]
