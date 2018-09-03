from django.urls import path, include

urlpatterns = [
    path('common/', include('apps.common.api.1-0.urls'))
]
