from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('insurance/', include('insurance.urls')),
    path('admin/', admin.site.urls)
]
