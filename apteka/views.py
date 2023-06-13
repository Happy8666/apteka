from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from .models import Medication, Customer, CustomerForm, Order

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication_list.html', {'medications': medications})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

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
    return render(request, 'apteka/success.html')

# Другие представления для управления складом, поставками и т.д.

def sell_product(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Создаем новый объект Customer с данными из формы
            customer = form.save()

            # Другая логика для обработки продажи товара

            return redirect('success')  # Перенаправление на страницу успешной продажи
    else:
        form = CustomerForm()

    return render(request, 'sell_product.html', {'form': form})