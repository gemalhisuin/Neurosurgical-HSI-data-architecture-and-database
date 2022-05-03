from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('category/<str:pk>', views.categoryPage, name='image-category'),
    # path('category/<slug:slug1>/<slug:slug2>', views.imageDetailPage, name='image-detail'),
    path('spectral', views.spectralPage, name='spectral-info'),
    path('search', views.searchPage, name='search-page'),
    path('search2', views.searchPage2, name='search-page2'),
    path('spectralinfo/<int:pk>', views.testPage, name='test-page'),

]