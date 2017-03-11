from django.conf.urls import *
from massivemap import views
from djgeojson.views import GeoJSONLayerView

from massivemap.models import WeatherStation


urlpatterns = [url(r'^test/$', views.map_start),
               url(r'^t2/$', views.map_test),
               url(r'^plain/$', views.map_plain),
               url(r'^fancy/$', views.map_fancy),
               url(r'^data.geojson$', GeoJSONLayerView.as_view(model=WeatherStation), name='data')]