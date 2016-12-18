from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    url(r'^user_home/$', TemplateView.as_view(template_name='user_home.html'), name='user_home'),
    url(r'^admin/', admin.site.urls),
]