from django.urls import path

from searchengine import views

app_name = 'searchengine'
urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('ajax/search/', views.ajax_search, name='ajax_search'),
    path('search/', views.search, name='search'),
]
