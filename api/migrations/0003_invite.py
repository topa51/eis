# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160331_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('key', models.CharField(max_length=255)),
                ('deeplink', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
