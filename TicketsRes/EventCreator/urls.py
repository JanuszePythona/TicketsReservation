from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^add_sector/(?P<event_id>[0-9]+)$', views.add_sector, name='add_sector'),
    url(r'^confirm_cancel/(?P<event_id>[0-9]+)$', views.confirm_cancel, name='confirm_cancel'),
    url(r'^cancel_event/(?P<event_id>[0-9]+)$', views.cancel_event, name='cancel_event')
]
