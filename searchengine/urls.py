from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from searchengine import views

app_name = 'searchengine'
urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('ajax/search/', views.ajax_search, name='ajax_search'),
    path('search/', views.search, name='search'),
    path('book/<int:book_id>', views.book, name='book'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)