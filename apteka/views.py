from django.shortcuts import render
from .models import Medication, Customer, Order

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'apteka/medication_list.html', {'medications': medications})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'apteka/customer_list.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'apteka/order_list.html', {'orders': orders})

def home(request):
    return render(request, 'interface.html')

# Другие представления для управления складом, поставками и т.д.
