from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.AuthorsListView.as_view(), name='list-authors'),
]