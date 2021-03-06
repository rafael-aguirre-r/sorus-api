from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('offers/', include('offers.urls')),
    path('sales/', include('sales.urls')),
]
