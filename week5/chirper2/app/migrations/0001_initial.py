# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chirp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
