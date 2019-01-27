from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from .search import BookIndex, PageIndex
from .models import Page, Book
# from .helper import get_search_results

# Create your views here.

def index(request):
    context = {}
    return render(request, 'searchengine/index.html', context)


def contact(request):
    context = {}
    return render(request, 'searchengine/contact.html', context)

def search(request):
    context = {}
    # Check and retrieve the query value from GET q 
    # if not request.GET.get('q', None):
    #     return redirect('searchengine:index')
    # else:
    #     q = request.GET.get('q', None).strip()
    q = request.GET.get('q',None)
    # lan = request.GET.get('language',None)
    para = request.GET.get('parameter',None)

    print(lan)
    if q is None:
        return redirect('searchengine:index')
    if para == 'author':
        a = BookIndex.search().query('match_phrase',author=q)
        ids = [i.id for i in a]
        context['results'] = Book.objects.filter(id__in=ids)
    elif para == 'title':
        a = BookIndex.search().query('match_phrase',title=q)
        ids = [i.id for i in a]
        context['results'] = Book.objects.filter(id__in=ids)
    else:
        a=PageIndex.search().query('match_phrase',content=q)
        ids=[i.id for i in a]
        context['results'] = Book.objects.filter(pages__id__in=ids).distinct()

    # if not q :
    #     return redirect("searchengine:index")
    # else : 
    #     q = BookIndex.search().query("match",title=q)

    context['q'] = q
    # results = get_search_results(q)
    # context['nresults'] = len(a)
    # context['results'] = a
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
