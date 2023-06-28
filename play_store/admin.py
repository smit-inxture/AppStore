from django.contrib import admin

from play_store.models import AppPackage,AppDetails,AppComments

# Register your models here.

admin.site.register(AppPackage)
admin.site.register(AppDetails)
admin.site.register(AppComments)