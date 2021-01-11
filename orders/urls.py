from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('add/<item_id>/', views.add_to_order, name='add_to_order'),
    # path('update/<order_id>/', views.update_order, name='update_order'),
    path('remove/<order_id>/', views.remove_from_order,
         name='remove_from_order'),

]
