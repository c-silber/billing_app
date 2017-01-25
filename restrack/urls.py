from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<facility_id>[0-9]+)/facility/$', views.facility, name='facility'),
	url(r'^(?P<facility_id>[0-9]+)/resident/$', views.resident, name='resident'),
]