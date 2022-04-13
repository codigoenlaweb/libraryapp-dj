from django.contrib import admin
from apps.Books.models import Books, Categorys

# Register your models here.
@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    '''Admin View for Categorys'''

    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 30


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    '''Admin View for Books'''

    list_display = ('title', 'views',)
    list_filter = ('category',)
    filter_horizontal = ('author', 'category')
    search_fields = ('title',)
    list_per_page = 20
    
    
    
    