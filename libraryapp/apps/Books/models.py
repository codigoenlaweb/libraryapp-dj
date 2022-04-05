from django.db import models

from apps.Authors.models import Authors

# Create your models here.
class Categorys(models.Model):
    """Model definition for Categorys."""
    name = models.CharField(verbose_name='Category name', max_length=18)
    

    class Meta:
        """Meta definition for Categorys."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Categorys."""
        return  f'{self.name}'
    
    
class Books(models.Model):
    """Model definition for Books."""

    category = models.ManyToManyField(Categorys, verbose_name="Category")
    author = models.ManyToManyField(Authors)
    title = models.CharField(verbose_name='Book title', max_length=30)
    release_date = models.DateField(verbose_name='book release date')
    cover_page = models.ImageField(upload_to='cover',)
    views = models.PositiveIntegerField(verbose_name='Views', default=0)

    class Meta:
        """Meta definition for Books."""

        verbose_name = 'Books'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Books."""
        return f''

