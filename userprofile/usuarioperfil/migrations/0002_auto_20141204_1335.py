# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioperfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zona_horaria',
            field=timezone_field.fields.TimeZoneField(default=b'America/Los_Angeles'),
            preserve_default=True,
        ),
    ]
