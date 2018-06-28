from django.conf.urls import url
from ..setForSummer_app import views

urlpatterns = [
    url(r'^setHome$', views.setHome),
    url(r'^food$', views.food),
    url(r'^activities$', views.activities),
    url(r'^map/(?P<id>\w+)$', views.map_id),
    url(r'^map/activities/(?P<id>\w+)$', views.activities_map),
    url(r'^learning$', views.learning),
    url(r'^faqs$', views.faqs),
    url(r'^contact$', views.contact),
]