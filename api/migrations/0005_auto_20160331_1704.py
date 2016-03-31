# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160331_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='ip',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invite',
            name='unixTimestamp',
            field=models.IntegerField(default=1459443850),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=models.IntegerField(default=1459443850),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.IntegerField(default=1459443850),
        ),
    ]
