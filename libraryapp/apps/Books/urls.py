from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='list-books'),
]