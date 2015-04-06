import sys
reload(sys) 
sys.setdefaultencoding("utf-8") 

from django.db import models

from django.contrib.auth.models import User


class Blog(models.Model):
    category = models.ForeignKey('Category',related_name='category_set')
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('Blog_user',related_name='author_set')
    view_count=  models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
class Category(models.Model):
    name= models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('Blog_user',related_name='blog_set')
    def __unicode__(self):
        return self.name    
    
class Blog_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default='This guy is too lazy to levave anything here.')
    # photo=models.ImageField(upload_to="upload_imgs/" , default="upload_imgs/user-1.jpg")
    # file = models.FileField()
    def __unicode__(self):
        return self.user.username   


# class Item(models.Model):
#     name = models.CharField()
#     description = models.TextField()
#
#     class Meta:
#         ordering = ['name']
#
#     def __unicode__(self):
#         return  self.name
#
#     def get_absolute_url(self):
#         return  ('item_detail',None,{'object_id':self.id})
#
# class Photo(models.Model):
#     item = models.ForeignKey(Item)
#     title = models.CharField(max_length=100)
#     image = models.CharField(max_length=250, blank=True)
#     caption = models.CharField(max_length=250, blank=True)
#
#     class Meta:
#         ordering = ['title']
#
#     def __unicode__(self):
#         return  self.title
#
#     def get_absolute_url(self):
#         return  ('photo_detail', None, {'object_id:self.id'})
#
# class PhotoInLine(admin.StackedInline):
#     model = Photo
#
# class ItemAdmin(admin.ModelAdmin):
#     inlines =[PhotoInLine]
#
# admin.site.register(Item, ItemAdmin)
# admin.site.register(Photo)
