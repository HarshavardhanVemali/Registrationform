from django.contrib import admin
from .models import Register

class AverageUpdatedFilter(admin.SimpleListFilter):
    title = 'Average Updated'
    parameter_name = 'average_updated'

    def lookups(self, request, model_admin):
        return (
            ('updated', 'Updated'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'updated':
            return queryset.exclude(average__isnull=True)
        return queryset

class AdminRegister(admin.ModelAdmin):
    list_display = ('register_number', 'name', 'email', 'branch', 'year', 'concept_to_present', 'slot_number', 'evalutor_1', 'evalutor_2', 'average')
    list_filter = ('register_number', 'name', 'email', 'branch', 'year', 'concept_to_present', 'slot_number', 'average', AverageUpdatedFilter)
    search_fields = ('register_number', 'name', 'email', 'branch', 'year', 'concept_to_present', 'slot_number')

admin.site.register(Register, AdminRegister)

