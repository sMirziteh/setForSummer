from django.conf.urls import url
from ..setForSummer_app import views

urlpatterns = [
    url(r'^setHome$', views.setHome),
    url(r'^food$', views.food),
    url(r'^activities$', views.activities),
<<<<<<< HEAD
    url(r'^map$', views.map),
=======
    url(r'^map/(?P<id>\w+)$', views.map_id),
>>>>>>> 4ae15c9e26500c0fee78e408e18ad10d5a46a5ef
]