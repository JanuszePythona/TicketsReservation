from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/(?P<event_id>[0-9]+)$', views.view_event, name='view_event'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^user_home/$', views.user_home, name='user_home'),
    url(r'^place_reservation/(?P<event_id>[0-9]+)$', views.place_reservation, name='place_reservation'),
    url(r'^success_res/$', TemplateView.as_view(template_name='success_res.html')),
]
