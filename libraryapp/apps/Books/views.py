from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from .models import Books, Categorys
from apps.Authors.models import Authors
from django.urls import reverse_lazy
from .forms import CateoryForm
# Create your views here.


class BooksListView(ListView):
    template_name = "books/list-books.html"
    context_object_name = 'books'

    def get_queryset(self):
        name = self.request.GET.get("name")

        queryset = Authors.objects.order_by()
        return queryset


class CategorysCreateView(CreateView):
    model = Categorys
    template_name = "books/category-model.html"
    fields = '__all__'
    success_url = reverse_lazy('book:category-model')


class CategorysFormView(FormView):
    form_class = CateoryForm
    template_name = "books/category-form.html"
    success_url = reverse_lazy('book:category-form')

    def form_valid(self, form):
        Categorys.objects.create(
            name=form.cleaned_data['name']
        )
        
        return super().form_valid(form)