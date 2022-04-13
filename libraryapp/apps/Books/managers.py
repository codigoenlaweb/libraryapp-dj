from django.db import models
from django.db.models import Q, Count


class BooksManager(models.Manager):
    ''' Managers for Books '''

    def list_books(self):
        return self.all()

    def list_books_filter(self, name, date1, date2):
        if name == None:
            name = ''

        if date1 == None:
            date1 = ''

        if date2 == None:
            date2 = ''

        return self.filter(title__contains=name, release_date__year__range=(date1, date2))

    def book_by_category(self, category):
        if category == None:
            category = ''
            
        return self.filter(category__name__contains=category, author__name__contains='Holly')

    def algo(self):
        return self.filter(author__name__contains='Holly').aggregate(total_count=Count('id'))

    # def list_books_filter2(self, name):
    #     if name == None:
    #         name = ''

    #     return self.filter(
    #         Q(name__contains=name) | Q(last_name__contains=name)
    #     )

    # def list_books_filter3(self, name):
    #     if name == None:
    #         name = ''

    #     return self.filter(
    #         Q(name__contains=name) | Q(last_name__contains=name)
    #     ).filter(age__lt=51)
