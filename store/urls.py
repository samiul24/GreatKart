from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.store, name='store' ),
    path('categories/<slug:category_slug>/', views.store, name='store_by_category'),
    path('categories/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),

]