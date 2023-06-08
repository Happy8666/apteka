from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('medications/', views.medication_list, name='medication_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),
    path('InventoryManager/', views.InventoryManager.as_view(), name='InventoryManager'),

    # Другие URL-шаблоны для других представлений
    path('InventoryManager/add_medication/', views.InventoryManager.add_medication, name='add_medication'),
    path('InventoryManager/edit_medication/<int:medication_id>/', views.InventoryManager.edit_medication, name='edit_medication'),
    path('InventoryManager/delete_medication/<int:medication_id>/', views.InventoryManager.delete_medication, name='delete_medication'),
]
