# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=255)),
                ('deeplink', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=65)),
                ('courseAngle', models.DecimalField(decimal_places=2, max_digits=65)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=65)),
                ('lng', models.DecimalField(decimal_places=2, max_digits=65)),
                ('name', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
