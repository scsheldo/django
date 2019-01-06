from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('amaraspa.studio/', include('amaraspa.urls')),
    path('admin/', admin.site.urls),
]
