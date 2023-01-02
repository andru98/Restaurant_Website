from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from . models import Post, Category,Comment
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields= '__all__'
    list_display = ['title','category','author','created']
    search_fields = ['title','content']
    list_filter = ('category',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)