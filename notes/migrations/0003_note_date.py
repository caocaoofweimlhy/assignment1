# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
