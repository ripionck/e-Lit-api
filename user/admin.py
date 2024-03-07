from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('email', 'username')

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = 'Full Name'

admin.site.register(CustomUser, CustomUserAdmin)