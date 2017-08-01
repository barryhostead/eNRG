# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('High', models.BooleanField()),
                ('Medium', models.BooleanField()),
                ('Low', models.BooleanField()),
                ('Score', models.IntegerField()),
                ('Notes', models.TextField()),
            ],
        ),
    ]
