# from django.contrib import admin
import xadmin
from Myblog import  models
class Blog_admin(object):
    list_display=('title','summary','author','signature','view_count','created_at')
    list_filter=('created_at',)
    search_fields =('title','author__user__username')

    def signature(self,obj):
        return obj.author.signature
    signature.short_description  = 'hah'

xadmin.site.register(models.Blog, Blog_admin)
xadmin.site.register(models.Category)
xadmin.site.register(models.Blog_user)
