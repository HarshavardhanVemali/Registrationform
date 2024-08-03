from django.contrib import admin
from .models import Register

class AdminRegister(admin.ModelAdmin):
    list_display =('register_number','name','email','branch','year','concept_to_present','slot_number','evalutor_1','evalutor_2','average')
    list_filter =('register_number','name','email','branch','year','concept_to_present','slot_number')
    search_fields = ('register_number','name','email','branch','year','concept_to_present','slot_number')

admin.site.register(Register,AdminRegister)
