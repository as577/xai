# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explainable', '0005_explainablemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='explainablemodel',
            name='model_color',
            field=models.CharField(default='#000000', max_length=200),
            preserve_default=False,
        ),
    ]
