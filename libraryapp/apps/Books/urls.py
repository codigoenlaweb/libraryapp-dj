from django.urls import path, include
from . import views

app_name='book'
urlpatterns = [
    path('', views.BooksListView.as_view(), name='list-books'),
    path('model-category', views.CategorysCreateView.as_view(), name='category-model'),
    path('form-category', views.CategorysFormView.as_view(), name='category-form'),
]