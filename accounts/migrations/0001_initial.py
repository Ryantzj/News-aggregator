# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.CharField(max_length=2)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('deleted', models.CharField(max_length=20)),
                ('permission', models.CharField(max_length=2)),
            ],
        ),
    ]
