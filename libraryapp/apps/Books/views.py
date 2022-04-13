from django.shortcuts import render
from django.views.generic import ListView
from .models import Books
# Create your views here.


class BooksListView(ListView):
    template_name = "books/list-books.html"
    context_object_name = 'books'
    
    def get_queryset(self):
        name = self.request.GET.get("name")

        queryset = Books.objects.list_books()
        return queryset