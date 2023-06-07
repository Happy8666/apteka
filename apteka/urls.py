from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='interface.html'),
    path('medications/', views.medication_list, name='medication_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),

    # Другие URL-шаблоны для других представлений
]
