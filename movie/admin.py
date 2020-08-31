from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movies,Review,Profile,ProfileDislikedMovie,ProfileLikedMovie
# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfileDislikedMovie)
admin.site.register(ProfileLikedMovie)
admin.site.register(Review)
@admin.register(Movies)
class MovieName(ImportExportModelAdmin):
    pass
