# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commentID', models.CharField(max_length=2)),
                ('commentContent', models.CharField(max_length=50)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.CharField(max_length=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postID', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=50)),
                ('postContent', models.CharField(max_length=50)),
                ('rankingPoints', models.IntegerField(default=0)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.CharField(max_length=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
