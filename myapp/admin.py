from django.contrib import admin

from .models import WorkRequest, Area, Plant, Category, Status, BusinessUnit

# Register your models here.
admin.site.register({Area, Plant, Category, Status, BusinessUnit})


@admin.register(WorkRequest)
class WorkRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'status', 'area', 'business_unit')
    list_filter =  ('status', 'business_unit', 'area')
    search_fields = ('title',)
    fields = ('title', ('business_unit', 'category'), ('status', 'plant', 'area'))
