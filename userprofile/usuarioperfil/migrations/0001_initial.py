# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.PositiveIntegerField()),
                ('provincia', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
                ('zona_horaria', timezone_field.fields.TimeZoneField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
