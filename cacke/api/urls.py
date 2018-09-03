from django.urls import path, include


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('v1.0/', include('apps.v1-0'), name='v1.0')
]
