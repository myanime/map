from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from popup import views


urlpatterns = ['',
               url(r'^test/$','map.views.test'),
               url(r'test2/$','map.views.test2'),
               url(r'^(?P<post_id>\d+)', 'map.views.post'),
               url(r'^api/$', views.PostList.as_view()),
               url(r'^api/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
               ]

urlpatterns = format_suffix_patterns(urlpatterns)


