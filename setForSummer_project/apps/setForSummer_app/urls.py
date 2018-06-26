from django.conf.urls import url
from ..setForSummer_app import views

urlpatterns = [
    url(r'^setHome$', views.setHome),
    url(r'^food$', views.food),
    url(r'^activities$', views.activities),
]