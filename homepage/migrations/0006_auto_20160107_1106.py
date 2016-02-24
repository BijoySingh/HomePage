# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20160107_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ip', models.CharField(max_length=100, blank=True)),
                ('visit_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Access',
        ),
    ]
