# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_card_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewCategory',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('score', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='homepage.ReviewCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
