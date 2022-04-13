from django.db import models
from apps.Books.models import Books

# Create your models here.


class Readers(models.Model):
    """Model definition for Readers."""

    name = models.CharField(verbose_name='Reader name', max_length=50)
    last_name = models.CharField(
        verbose_name='Reader last name', max_length=50)
    nationality = models.CharField(
        verbose_name='Reader nationality', max_length=18)
    age = models.PositiveIntegerField(verbose_name='Reader age', default=0)

    class Meta:
        """Meta definition for Readers."""

        verbose_name = 'Readers'
        verbose_name_plural = 'Readerss'

    def __str__(self):
        """Unicode representation of Readers."""
        pass


class Loan(models.Model):
    """Model definition for Loan."""

    reader = models.ForeignKey(
        Readers, verbose_name='Reader', on_delete=models.CASCADE)
    book = models.ForeignKey(
        Books, verbose_name='Book', on_delete=models.CASCADE)
    loan_date = models.DateField(verbose_name='Loan date')
    return_date = models.DateField(verbose_name='Return date')
    returned = models.BooleanField(verbose_name='Returned', default=False)

    class Meta:
        """Meta definition for Loan."""

        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'

    def __str__(self):
        """Unicode representation of Loan."""
        return f'{self.returned}'
