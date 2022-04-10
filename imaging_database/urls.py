from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.categoryPage, name='image-category'),
    path('category/<slug:slug1>/<slug:slug2>', views.imageDetailPage, name='image-detail'),
    path('category/<slug:slug3>/<slug:slug4>/<slug:slug5>', views.spectralPage, name='spectral-info'),
    path('search', views.searchPage, name='search-page'),

]