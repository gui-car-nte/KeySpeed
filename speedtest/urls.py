from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls', namespace='api')),
    path('profiles/', include('profiles.urls')),
    path('ranking/', include('ranking.urls')),
]
