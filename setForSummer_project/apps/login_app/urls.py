from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^processRegistration$', views.processReg),
    # url(r'^success$', views.wall_index), #put route in non-login urls.py
    url(r'^login$', views.login),
    url(r'^reset$', views.reset),
]