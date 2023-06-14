from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.forms import formset_factory
from .forms import SearchForm, OrderForm, SellProductFormSet
from .models import Medication, Customer, CustomerForm, Order, SellProductForm

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication_list.html', {'medications': medications})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def delete_customer(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            return redirect('customer_list')
        except Customer.DoesNotExist:
            pass
    return redirect('customer_list')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def add_item(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')

        try:
            order = Order.objects.get(id=order_id)
            medication = Medication.objects.get(id=item_id)
            order.items.create(medication=medication, quantity=quantity)
        except (Order.DoesNotExist, Medication.DoesNotExist):
            pass

    return redirect('order_list')

def delete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
    except Order.DoesNotExist:
        pass

    return redirect('order_list')

def create_order(request):
    # Ваша логика создания заказа
    return render(request, 'order/create_order.html')

def main_menu(request):
    # Проверка аутентификации пользователя
    if not request.method:
        # Пользователь не аутентифицирован, перенаправление на страницу входа
        return redirect('login')
    
    # Если пользователь аутентифицирован, отображение главного меню
    return render(request, 'main_menu.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Проверка правильности учетных данных
        if username == 'admin' and password == 'qwe':
            # Если учетные данные верны, перенаправляем на страницу основного меню
            return redirect('main_menu')
        else:
            # Если учетные данные неверны, отображаем сообщение об ошибке
            error_message = 'Неверное имя пользователя или пароль!'
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')

# Другие представления для управления складом, поставками и т.д.

def sell_product(request):
    SearchFormSet = formset_factory(SearchForm, extra=1)
    
    if request.method == 'POST':
        formset = SearchFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get('quantity') > 0:
                    medication_id = form.cleaned_data.get('medication_id')
                    quantity = form.cleaned_data.get('quantity')
                    medication = Medication.objects.get(id=medication_id)
                    # выполнение логики продажи товара
                    # ...
            return redirect('success')
    else:
        formset = SearchFormSet()

    return render(request, 'sell_product.html', {'formset': formset})

def autocomplete(request):
    term = request.GET.get('term', '')
    medications = Medication.objects.filter(name__icontains=term)[:10]  # Получить до 10 предложений
    results = [medication.name for medication in medications]
    return JsonResponse(results, safe=False)