from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from usuarioperfil.views import UserprofileCreate, UserprofileList, UserprofileUpdate, UserUpdate
from usuarioperfil.views import UserprofileDelete
from usuarioperfil import views
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'userprofile.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^new$', UserprofileCreate.as_view(), name = 'create_user'),
    url(r'^usuario$', UserprofileList.as_view(), name = 'list_user'),
    url(r'^signup$', 'usuarioperfil.views.signup', name='signup'),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^home$', 'usuarioperfil.views.home', name='home'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(r'^$', 'usuarioperfil.views.main', name='main'),
    url(r'^detalle(?P<Userprofile_id>\d+)$', 'usuarioperfil.views.UserDetail', name='detail_user'),
    url(r'^detalle(?P<pk>\d+)/update$', UserprofileUpdate.as_view(), name='update_user'),
    url(r'^usuario(?P<pk>\d+)/update$', UserUpdate.as_view(), name='update_useri'),
    url(r'^detalle(?P<pk>\d+)/delete$', UserprofileDelete.as_view(), name='delete_user'),

)
