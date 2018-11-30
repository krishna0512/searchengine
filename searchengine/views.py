from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages

from .models import Page, Book
from .helper import get_search_results

# Create your views here.

def index(request):
    context = {}
    return render(request, 'searchengine/index.html', context)

def search(request):
    context = {}
    # Check and retrive the query value from GET q 
    if not request.GET.get('q', None):
        return redirect('searchengine:index')
    else:
        q = request.GET.get('q', None).strip()
    context['q'] = q
    results = get_search_results(q)
    context['nresults'] = results.count()
    context['results'] = results
    return render(request, 'searchengine/search.html', context)

def ajax_search(request):
    data = {
            'results': [],
            'error_message': '',
            'nresults': 0
            }
    if not request.GET.get('q', None):
        data['error_message'] = 'No Search Query Given'
        return JsonResponse(data)
    else:
        q = request.GET.get('q', None).strip()
        print('Page database is searching against query: "{}"'.format(query))

    results = get_search_results(q)
    data['nresults'] = results.count()
    if data['nresults'] == 0:
        data['error_message'] = 'No results found, Please redefine your Search'
        return JsonResponse(data)
    for i in results:
        data['results'].append( {
            'pageid': i.id,
            'pagetitle': i.pagetitle,
            'book': i.book.title,
        })
    return JsonResponse(data)

def book(request, book_id):
    context = {}
    try:
        b = Book.objects.get(pk=book_id)
    except:
        messages.error(request, 'No book with this ID')
        return redirect(request.META.get('HTTP_REFERER','/'))
    context['book'] = b
    return render(request, 'searchengine/book.html', context)
