from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from .models import Medication, Customer, Order

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
            error_message = 'Неверное имя пользователя или пароль'
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
# Другие представления для управления складом, поставками и т.д.

class InventoryManager(View):
    def get(self, request):
        medications = Medication.objects.all()
        return render(request, 'apteka/medication_list.html', {'medications': medications})

    def post(self, request):
        pass

    def add_medication(self, request):
        if request.method == 'POST':
            # Get data from the form and create a new Medication object
            # ...

            # Save the object to the database
            # ...

            # Redirect to the medication list page
            return redirect('medication_list')

        return render(request, 'add_medication.html')

    def edit_medication(self, request, medication_id):
        medication = Medication.objects.get(id=medication_id)

        if request.method == 'POST':
            # Получить данные из формы и обновить объект Medication
            # ...

            # Сохранить объект в базе данных
            # ...

            # Перенаправить на страницу со списком товаров
            return redirect('medication_list')
        
        return render(request, 'apteka/edit_medication.html', {'medication': medication})

    def delete_medication(self, request, medication_id):
        medication = Medication.objects.get(id=medication_id)

        if request.method == 'POST':
            # Удалить объект Medication из базы данных
            # ...

            # Перенаправить на страницу со списком товаров
            return redirect('medication_list')
        
        return render(request, 'apteka/delete_medication.html', {'medication': medication})
