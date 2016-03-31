# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_ship_unixtimestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Janusz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('januszType', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=2, max_digits=65)),
                ('lng', models.DecimalField(decimal_places=2, max_digits=65)),
                ('count', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('unixTimestamp', models.IntegerField(default=1459430003)),
            ],
        ),
        migrations.AlterField(
            model_name='ship',
            name='unixTimestamp',
            field=models.IntegerField(default=1459430003),
        ),
    ]
