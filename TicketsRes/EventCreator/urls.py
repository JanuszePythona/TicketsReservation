from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_event/$', views.add_event, name='add_event'),
]
