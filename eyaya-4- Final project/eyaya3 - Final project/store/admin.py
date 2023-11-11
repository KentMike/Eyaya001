from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Catergory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields ={'slug':('name',)}

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn','slug','copies', 
                    'in_stock','created','updated']
    list_filter = ['in_stock','is_active']
    list_editable = ['copies','in_stock']
    prepopulated_fields ={'slug':('title',)}