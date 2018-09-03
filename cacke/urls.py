from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from .api import urls

urlpatterns = [
]

apps_patterns = i18n_patterns(
    path('', include('apps.common.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
)

urlpatterns += apps_patterns
