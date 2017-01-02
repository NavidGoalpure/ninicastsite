from django.contrib import admin

from .models import itssafeCategories
from .models import itssafePosts
import os


class itssafeAdmin (admin.ModelAdmin):
    list_display = ('categoryName','categoryID')
    list_editable = ('categoryName',)
    list_display_links = ('categoryID',)

class itssafePostsAdmin (admin.ModelAdmin):
    list_display = ('id','titr','categoryName','categoryCode','publication_date','audio')
    list_filter = ('categoryName',)
    search_fields = ('titr',)



admin.site.register(itssafeCategories, itssafeAdmin)
admin.site.register(itssafePosts, itssafePostsAdmin)