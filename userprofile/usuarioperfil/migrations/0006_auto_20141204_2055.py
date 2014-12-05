# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioperfil', '0005_auto_20141204_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('list_zet', 'Can view list ap'), ('view_zet', 'Can view ap'), ('add_zet', 'Can add Zeto'), ('change_zet', 'Can change ap'), ('delete_zet', 'Can delete ap'))},
        ),
    ]
