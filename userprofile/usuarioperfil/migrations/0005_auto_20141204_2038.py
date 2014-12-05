# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioperfil', '0004_userprofile_useri'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('list_zet', 'Can view list ap'), ('view_zet', 'Can view ap'), ('add_zet', 'Can add ap'), ('change_zet', 'Can change ap'), ('delete_zet', 'Can delete ap'))},
        ),
    ]
