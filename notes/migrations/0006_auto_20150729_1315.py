# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20150716_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(related_name='notes', blank=True, to='notes.Folder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(related_name='notes', null=True, to='notes.Tag', blank=True),
            preserve_default=True,
        ),
    ]
