# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=65)),
                ('courseAngle', models.DecimalField(decimal_places=2, max_digits=65)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=65)),
                ('lng', models.DecimalField(decimal_places=2, max_digits=65)),
                ('name', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
