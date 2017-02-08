from django.contrib import admin
from .models import *

# Register your models here.


class UrlShortenAdmin(admin.ModelAdmin):
    list_display = ('user_url','url_code','nike_name','nb_access','date_creation')
    list_filter = ('nike_name',)
    date_hierarchy = 'date_creation'
    ordering = ('date_creation',)
    search_fields = ('user_url',)




admin.site.register(UrlShort,UrlShortenAdmin)
