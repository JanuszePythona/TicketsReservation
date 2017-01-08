from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/(?P<event_id>[0-9]+)$', views.view_event, name='view_event'),
    url(r'^about$', views.about, name='about'),
    url(r'^user_home/$', views.user_home, name='user_home'),

]
