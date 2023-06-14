from django.urls import path
from . import views

urlpatterns = [
    #############################################################################
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('main_menu', views.main_menu, name='main_menu'),
    #############################################################################

    path('medication_list', views.medication_list, name='medication_list'),

    #############################################################################

    path('customers', views.customer_list, name='customer_list'),
    path('delete_customer/', views.delete_customer, name='delete_customer'),

    #############################################################################

    path('order/list/', views.order_list, name='order_list'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('order/add-item/', views.add_item, name='add_item'),

    #############################################################################

    path('sell_product/', views.sell_product, name='sell_product'),
    path('success/', views.success, name='success'),
    path('sell_product/autocomplete/', views.autocomplete, name='autocomplete'),
]
