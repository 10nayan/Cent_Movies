from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movies,Review
# Register your models here.
@admin.register(Movies)
class MovieName(ImportExportModelAdmin):
    pass
admin.site.register(Review)