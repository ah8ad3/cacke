from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
]


apps_patterns = i18n_patterns(
    # Your APIs come here
    path('', include('apps.common.urls')),
    path('admin/', admin.site.urls)
)

urlpatterns += apps_patterns
