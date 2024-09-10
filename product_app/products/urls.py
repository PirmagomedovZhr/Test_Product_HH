from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('products/', views.list_products),
    path('products/create/', views.create_product),
]
