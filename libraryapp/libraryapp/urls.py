from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('apps.Authors.urls')),
    path('book/', include('apps.Books.urls')),
]
