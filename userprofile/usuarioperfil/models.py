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
            ('list_app', 'Can view list app'),
            ('view_app', 'Can view app'),
            ('add_app', 'Can add app'),
            ('change_app', 'Can change app'),
            ('delete_app', 'Can delete app'),
        )

    def __unicode__(self):
        return u"%s" % self.useri
    @models.permalink
    def get_absolute_url(self):
        return ('detail_user', [int(self.pk)])
