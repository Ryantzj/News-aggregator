# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
    ]
