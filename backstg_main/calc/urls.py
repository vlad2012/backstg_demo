from django.conf.urls import patterns, url
from calc import views

urlpatterns = [
  url(r'^difference/$', views.calc_list),
  url(r'^difference/(?P<number>[0-9]+)/$', views.calc_detail),
]


