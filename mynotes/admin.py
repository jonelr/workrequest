from django.contrib import admin

from .models import Training


# Register your models here.
@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_taken', 'account')
    search_fields = ('title',)
    exclude = ('account',)

    def save_model(self, request, obj, form, change):
        if not obj.account:
            obj.account = request.user
        super(TrainingAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TrainingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(account=request.user)
