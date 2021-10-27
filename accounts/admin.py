# accounts/admin.py

from .models import Permissions, Role
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
CustomUser = get_user_model()

from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username', 'role',) 
    list_filter = ('email', 'username', 'role', 'is_active', 'is_staff',)
    ordering = ('username',) 
    fieldsets = (
        (None, {
            "fields": ('email', 'username', 'role', 'is_active', 'is_staff',),
        }),
        ('permissions', {
            "fields": ('groups',)
        }),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'role', 'is_active', 'is_staff',)
        }),
       
            
        
    )
    

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


class RoleInline(admin.TabularInline):
    model = Role.permissions.through
    extra = 1


class PermissionsAdmin(admin.ModelAdmin):
    inlines = [RoleInline]





# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser, CustomUserAdminConfig)

# admin.site.register(Permissions)
admin.site.register(Role)


# admin.site.register(Permissions, PermissionsAdmin)

admin.site.register(Permissions, PermissionsAdmin)
