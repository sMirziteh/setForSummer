from django.conf.urls import url
from ..setForSummer_app import views

urlpatterns = [
    url(r'^setHome$', views.setHome),
    url(r'^food$', views.food),
    url(r'^activities$', views.activities),
    url(r'^learning$', views.learning),
    url(r'^faqs$', views.faqs),
    url(r'^contact$', views.contact),
]