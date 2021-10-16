from django.contrib import admin
from django.urls import path, include
from django.views import debug

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('api.urls'), name='api'),
    path('hihi-django', debug.default_urlconf),
]
