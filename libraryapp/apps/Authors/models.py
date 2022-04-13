from django.db import models
from .managers import AuthorManager

# Create your models here.
class Authors(models.Model):
    """Model definition for Authors."""
    name = models.CharField(verbose_name='Author name', max_length=50)
    last_name = models.CharField(verbose_name='Author last name', max_length=50)
    nationality = models.CharField(verbose_name='Author nationality', max_length=20)
    age = models.PositiveIntegerField(verbose_name='Author age')
    
    ''' Managers '''
    objects = AuthorManager()


    class Meta:
        """Meta definition for Authors."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Authors."""
        return f'{self.name} {self.last_name}'
