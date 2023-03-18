from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('friends/', include('friends.urls')),
    path('registration/', include('registration.urls')),
    path('registration/', include('django.contrib.auth.urls')),
]
