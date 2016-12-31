from django.contrib import admin

from .models import itsNormalCategories
from .models import itsNormalPosts
import os


class itsNormalAdmin (admin.ModelAdmin):
    list_display = ('categoryName','categoryID')
    list_editable = ('categoryName',)
    list_display_links = ('categoryID',)

class itsNormalPostsAdmin (admin.ModelAdmin):
    list_display = ('id','titr','categoryName','categoryCode','publication_date','audio')
    list_filter = ('categoryName',)
    search_fields = ('titr',)



admin.site.register(itsNormalCategories, itsNormalAdmin)
admin.site.register(itsNormalPosts, itsNormalPostsAdmin)