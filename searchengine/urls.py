from django.urls import path

from searchengine import views

app_name = 'searchengine'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
]
