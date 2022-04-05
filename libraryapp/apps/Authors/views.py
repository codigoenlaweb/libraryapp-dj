from django.shortcuts import render
from django.views.generic import ListView
from apps.Authors.models import Authors
# Create your views here.


class AuthorsListView(ListView):
    template_name = "authors/list-authors.html"
    context_object_name = 'authors'
    
    def get_queryset(self):
        queryset = Authors.objects.all()
        return queryset
