from django.conf.urls import patterns, url, include
from pnd.views import *

urlpatterns = patterns('',
    url(r'^index/$', index, name='index'),
    url(r'^results/$', results, name='results'),
    url(r'^detail/$', detail, name='detail'),
)