# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.TextField(max_length=5000),
        ),
    ]
