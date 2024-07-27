# Handles the Django built in Admin interface
# Defines what gets displayed

from django.contrib import admin  
from .models import CustomUser, Group , ImageMetadata

@admin.register(CustomUser) 
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'gender']
    search_fields = ['username', 'email', 'phone']
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    pass

admin.site.register(ImageMetadata)

@admin.register(Group)
class GroupUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'groupbio', 'privacy', 'created_by' ]
    pass
