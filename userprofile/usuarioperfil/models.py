from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from timezone_field import TimeZoneField


# Create your models here.

class Userprofile(models.Model):
    useri = models.OneToOneField(User)
    telefono = models.PositiveIntegerField()
    provincia = models.CharField(max_length = 50)
    distrito = models.CharField(max_length = 50)
    departamento = models.CharField(max_length = 50)
    zona_horaria = TimeZoneField(default= 'America/Lima')
    class Meta:
        permissions = (
            ('list_zet', 'Can view list Zetto'),
            ('view_zet', 'Can view Zetto'),
            ('add_zet', 'Can add Zeto'),
            ('change_zet', 'Can change Zetto'),
            ('delete_zet', 'Can delete Zetto'),
        )

    def __unicode__(self):
        return u"%s" % self.useri
    @models.permalink
    def get_absolute_url(self):
        return ('detail_user', [int(self.pk)])
