# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20160108_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
