from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path
admin.site.site_header = "User-Role"
admin.site.site_title = "User-Role Admin"
admin.site.index_title = "Welcome to User-Role-Permissions Dashboard"







urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('django.contrib.auth.urls')),  # new
    # Local apps
    path('accounts/', include('accounts.urls')),  # new
    path('', include('pages.urls')),
]
