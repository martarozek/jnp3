from .base import *

DEBUG = False


USE_X_FORWARDED_HOST = True


USE_X_FORWARDED_PORT = True


ALLOWED_HOSTS = [
    'localhost',
]


INSTALLED_APPS += [
    'django.contrib.postgres',
]


DATABASES = {
    'default': {
        'ENGINE': 'django_postgrespool',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

DATABASE_POOL_ARGS = {
    'max_overflow': 10,
    'pool_size': 5,
    'recycle': 300,
}


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            'cache1:11211',
            'cache2:11212',
        ]
    }
}

STATIC_ROOT = '/code/static-files'
