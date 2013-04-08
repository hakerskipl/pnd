from django.conf.urls import patterns, url, include
from pnd.views import *

urlpatterns = patterns('',
    url(r'^index/$', index, name='index'),
    url(r'^results/$', results, name='results'),
    url(r'^detail/(?P<id>\d+)/$', detail, name='detail'),
    url(r'^feellucky/$', feelLucky, name='feelLucky'),

    url(r'^szukaj/$', search, name='search'),
    url(r'^typeahead/(?P<search>\w+)/$', typeahead, name='typeahead'),

    url(r'^fetch/$', fetchData, name='fetchData'),
)