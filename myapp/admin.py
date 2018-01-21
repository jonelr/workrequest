from django.contrib import admin

from .models import WorkRequest, Area, Plant, Category, \
    Status, BusinessUnit, Hours, TimeSheet, \
    SqlVersion, OsVersion, SqlServer, SqlLog, Landscape

# Register your models here.
admin.site.register({Area, Plant, Category, Status, BusinessUnit,
                     SqlVersion, OsVersion, Landscape })


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ('account', 'week_ending', 'hours')
    list_filter = ('account',)
    date_hierarchy = 'week_ending'


@admin.register(WorkRequest)
class WorkRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'status', 'area', 'business_unit')
    list_filter = ('status', 'business_unit', 'area')
    search_fields = ('title',)
    fields = ('title', ('business_unit', 'category'), ('status', 'plant', 'area'))


@admin.register(Hours)
class HoursAdmin(admin.ModelAdmin):
    date_hierarchy = 'week_ending'
    list_display = ('workrequest', 'week_ending', 'hours')
    list_filter = ('account',)
    fields = (('workrequest'), ('week_ending', 'hours'), 'notes')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.account = request.user
        super(HoursAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(HoursAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(account=request.user)


class SqlLogInline(admin.TabularInline):
    model = SqlLog


@admin.register(SqlLog)
class SqlLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time_added', 'account')
    list_filter = ('servers', 'account',)
    exclude = ('account', 'time_added')
    filter_horizontal = ('servers',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.account = request.user
        super(SqlLogAdmin, self).save_model(request, obj, form, change)


@admin.register(SqlServer)
class SqlServerAdmin(admin.ModelAdmin):
    list_display = ('online','name', 'os', 'version', 'cpu', 'ram', 'mes', 'sap')
    list_display_links = ('name',)
    list_filter = ('online', 'landscape', 'version', 'sap', 'mes')
    fields = (('name', ), ('os','version',), ('cpu', 'ram'), ('mes', 'sap', 'monitor','port'), 'landscape')
