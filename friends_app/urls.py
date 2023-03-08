from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('friends/', include('friends.urls')),
    path('admin/', admin.site.urls),
]
