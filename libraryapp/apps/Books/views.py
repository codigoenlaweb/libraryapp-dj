from django.shortcuts import render
from django.views.generic import ListView
from .models import Books
from apps.Authors.models import Authors
# Create your views here.


class BooksListView(ListView):
    template_name = "books/list-books.html"
    context_object_name = 'books'
    
    def get_queryset(self):
        name = self.request.GET.get("name")

        queryset = Authors.objects.order_by()
        return queryset