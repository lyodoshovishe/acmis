from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^(?:(?P<kind>p|f|u)(?:/(?P<category>\S))?)?$', views.post_list, name='post_list'),
  url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
  url(r'^(?P<kind>p|f)/(?P<category>\S)/new/$', views.post_new, name='post_new'),
  url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
