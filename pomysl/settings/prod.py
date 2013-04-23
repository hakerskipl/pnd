# Django settings for pomysl project.
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

COMPRESS_ROOT = PROJECT_DIR + '/../static/'

COMPRESS_OFFLINE = True

COMPRESS_YUI_BINARY = 'yui-compressor'
COMPRESS_CLOSURE_COMPILER_BINARY = 'java -jar ' + PROJECT_DIR +  '../bin/closure.jar', 
COMPRESS_CLOSURE_COMPILER_ARGUMENTS = ' --compilation_level SIMPLE_OPTIMIZATIONS'


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