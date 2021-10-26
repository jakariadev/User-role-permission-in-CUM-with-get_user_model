from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('django.contrib.auth.urls')),  # new
    # Local apps
    path('', include('pages.urls')),
]
