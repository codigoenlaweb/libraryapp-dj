from django.contrib import admin
from .models import Readers, Loan

# Register your models here.
@admin.register(Readers)
class ReadersAdmin(admin.ModelAdmin):
    '''Admin View for Readers'''

    list_display = ('name', 'last_name', 'nationality', 'age')
    search_fields = ('name', 'last_name')
    
    
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    '''Admin View for Loan'''

    list_display = ('reader', 'book', 'loan_date', 'return_date', 'returned')
    list_filter = ('returned',)
    # inlines = [
    #     Inline,
    # ]
    raw_id_fields = ('reader', 'book')
    search_fields = ('reader',)