from django.contrib import admin
from .models import Authors

# Register your models here.
@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    '''Admin View for Authors'''

    list_display = ('name', 'last_name', 'nationality', 'age')
    # list_filter = ('nationality',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name', 'last_name',)
    # date_hierarchy = ''
    ordering = ('-id',)