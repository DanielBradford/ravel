
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<item_id>', views.view_product, name='view_product')

]
