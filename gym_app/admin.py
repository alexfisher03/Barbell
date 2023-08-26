from django.contrib import admin
from .models import CustomUser, TableData, ImageMetadata

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'gender']
    search_fields = ['username', 'email', 'phone']
    pass


admin.site.register(TableData)
admin.site.register(ImageMetadata)
