from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from pnd.models import Place, Tags

sitemaps = {
    'informacje': FlatPageSitemap,
    'restauracje': GenericSitemap({'queryset': Place.objects.all()}, priority=0.5),
    'mozliwosci': GenericSitemap({'queryset': Tags.objects.all()}, priority=0.6),
}

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pnd.views.index', name='home'),
    url(r'^torun/', include('pnd.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)

# handler404 = 'pnd.views.Error404'
# handler500 = 'pnd.views.Error500'