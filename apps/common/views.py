from django.conf import settings
from django.shortcuts import render
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from .messages import SIMPLE

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def welcome(request):

    return render(request, 'index.html', {'message': SIMPLE.get('welcome')})
