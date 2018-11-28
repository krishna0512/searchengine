from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, blank=True)
    editor = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=5000, blank=True)
    language = models.CharField(max_length=20, blank=True)

    def __repr__(self):
        return '<Book: {} ({})>'.format(self.title, self.author)

    def __str__(self):
        return self.title
