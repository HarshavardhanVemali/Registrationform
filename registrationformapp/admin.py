from django.contrib import admin
from .models import Register

class AdminRegister(admin.ModelAdmin):
    list_display = ('register_number', 'name', 'email', 'branch', 'year')
    list_filter = ('register_number', 'name', 'email', 'branch', 'year')
    search_fields = ('register_number', 'name', 'email', 'branch', 'year')

admin.site.register(Register, AdminRegister)

