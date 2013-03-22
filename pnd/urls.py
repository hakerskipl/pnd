from django.conf.urls import patterns, url, include
from pnd.views import *

urlpatterns = patterns('',
    url(r'^index/$', index, name='index'),
    url(r'^results/$', index, name='results'),
    url(r'^detail/$', index, name='detail'),
)