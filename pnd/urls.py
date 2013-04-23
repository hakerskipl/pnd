from django.conf.urls import patterns, url, include
from pnd.views import *

urlpatterns = patterns('',
    url(r'^znajdz/$', index, name='index'),
    url(r'^wsystkie-mozliwosci/$', index, {'home': True}, name='all-tags'),
    url(r'^restauracje/(?P<slug>.+)/$', results, name='results'),
    url(r'^lokal/(?P<slug>.+)/$', detail, name='detail'),
    url(r'^feellucky/$', feelLucky, name='feelLucky'),

    url(r'^szukaj/$', search, name='search'),
    url(r'^typeahead/(?P<search>\w+)/$', typeahead, name='typeahead'),

    url(r'^404/$', Error404, name='404'),
    url(r'^500/$', Error500, name='500'),

    url(r'^fetch/$', fetchData, name='fetchData'),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^kontakt/$', 'flatpage', {'url': '/kontakt/'}, name='kontakt'),
    url(r'^reklama/$', 'flatpage', {'url': '/reklama/'}, name='reklama'),
    url(r'^regulamin/$', 'flatpage', {'url': '/regulamin/'}, name='regulamin'),
    url(r'^polityka-prywatnosci/$', 'flatpage', {'url': '/polityka-prywatnosci/'}, name='polityka-prywatnosci'),
    url(r'^cos-nowego/$', 'flatpage', {'url':'/cos-nowego/'}, name='cos-nowego'),
)