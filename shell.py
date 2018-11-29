from django.urls import reverse
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User

from searchengine.models import *
# from searchengine.forms import *
# import requests
import os
import sys
import random
# from tabulate import tabulate

setup_test_environment()

from django.test import Client
c = Client()

def populate_user_database():
    os.chdir('./searchengine/static/searchengine/books')
    for (root, _, files) in os.walk('.'):
        if root == '.':
            continue
        print(root.strip())
        print(len(files))
        print('-------------------')
        booktitle = root.strip('./ ')
        bookauthor = 'krishna'
        b = Book(title=booktitle, author=bookauthor)
        b.save()
        print('Processing the Pages of {}'.format(booktitle))
        for page in files:
            filepath = '{}/{}'.format(root.strip(), page.strip())
            print(filepath)
            with open(filepath, 'r') as f:
                r = f.readlines()
            r = [i.strip() for i in r]
            content = '\n'.join(r)
            if len(content)>5000:
                print('number of characters extended beyond 5000 to {} for {}'.format(len(content), filepath))
                return 0
            Page(pagetitle=page.strip(), content=content, book=b).save()
    os.chdir('../../../../')

def flush_user_database():
    p = Page.objects.all()
    if len(p):
        for i in p:
            i.delete()
    b = Book.objects.all()
    if len(b):
        for i in b:
            i.delete()
