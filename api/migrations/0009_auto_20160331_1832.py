# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20160331_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='unixTimestamp',
            field=django_unixdatetimefield.fields.UnixDateTimeField(),
        ),
        migrations.AlterField(
            model_name='janusz',
            name='unixTimestamp',
            field=django_unixdatetimefield.fields.UnixDateTimeField(),
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=django_unixdatetimefield.fields.UnixDateTimeField(),
        ),
    ]
