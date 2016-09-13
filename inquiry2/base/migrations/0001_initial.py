# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-11 02:45
from __future__ import unicode_literals

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mock_survey', base.models.MockSurveyField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('perception', models.PositiveSmallIntegerField()),
                ('satisfaction', models.PositiveSmallIntegerField()),
                ('comments', models.TextField()),
                ('version', models.PositiveSmallIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]