# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20160331_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='unixTimestamp',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.IntegerField(default=1459449656),
        ),
    ]
