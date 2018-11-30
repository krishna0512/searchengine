from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    editor = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=20, blank=True)

    def __repr__(self):
        return '<Book: {} ({})>'.format(self.title, self.author)

    def __str__(self):
        return self.title

class Page(models.Model):
    # pagetitle stores the name of the text file from which the body contents come from.
    pagetitle = models.CharField(max_length=100, default='')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')
    content = models.TextField()
