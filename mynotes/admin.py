from django.contrib import admin

from .models import Training


# Register your models here.
@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    pass
