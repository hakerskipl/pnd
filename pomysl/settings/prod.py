#-*- coding: utf-8 -*-
from common import *

DEBUG = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'pomysl.wsgi.application'

# Kompresja dla produkcyjnego
COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.yui.YUICSSFilter',
]

COMPRESSOR_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.jsmin.SlimItFilter',
    'compressor.filters.yui.YUIJSFilter',
    'compressor.filters.jsmin.JSMinFilter',
    'compressor.filters.closure.ClosureCompilerFilter',
]

COMPRESS_OUTPUT_DIR = 'min'

# Cahce dla produkcyjnego

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

GRAPPELLI_ADMIN_TITLE = u'Pomysł na dziś'