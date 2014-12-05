# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioperfil', '0006_auto_20141204_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('list_zet', 'Can view list Zetto'), ('view_zet', 'Can view Zetto'), ('add_zet', 'Can add Zeto'), ('change_zet', 'Can change Zetto'), ('delete_zet', 'Can delete Zetto'))},
        ),
    ]
