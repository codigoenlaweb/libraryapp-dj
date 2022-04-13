from django.db import models
from django.db.models import Q, Count


class AuthorManager(models.Manager):
    ''' Managers for authors '''

    def list_authors(self):
        return self.all()

    def list_authors_filter(self, name):
        if name == None:
            name = ''
        return self.filter(name__contains=name)

    def list_authors_filter2(self, name):
        if name == None:
            name = ''

        return self.filter(
            Q(name__contains=name) | Q(last_name__contains=name)
        )

    def list_authors_filter3(self, name):
        if name == None:
            name = ''

        return self.filter(
            Q(name__contains=name) | Q(last_name__contains=name)
        ).filter(age__lt=51)
        
        
    def order_by(self):
        return self.annotate(count_book=Count('author_book'))
