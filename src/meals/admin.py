from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Meals
from .models import Category

class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields= '__all__'
    list_display = ['name','people','preparation_time','price']
    search_fields = ['name','description']
    list_filter = ('category', 'people')


admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)