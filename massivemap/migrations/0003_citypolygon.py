# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 22:45
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massivemap', '0002_auto_20170311_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityPolygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
