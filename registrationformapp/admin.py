from django.contrib import admin
from .models import Register

class AdminRegister(admin.ModelAdmin):
    list_display =('name','email','branch','year','concept_to_present','slot_number')
    list_filter =('name','email','branch','year','concept_to_present','slot_number')
    search_fields = ('name','email','branch','year','concept_to_present','slot_number')

admin.site.register(Register,AdminRegister)
