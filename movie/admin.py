from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movies,Review,Profile,ProfileDislikedMovie,ProfileLikedMovie
# all the  models is registerd here to use in admin panel
admin.site.register(Profile)
admin.site.register(ProfileDislikedMovie)
admin.site.register(ProfileLikedMovie)
admin.site.register(Review)
#MovieName class is inherited from ImportExportModelAdmin to import/export  data to csv
@admin.register(Movies)
class MovieName(ImportExportModelAdmin):
    pass
