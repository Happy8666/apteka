import datetime
from django.db import models
from django import forms

class Medication(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    # Другие поля для лекарства

class Customer(models.Model):
    name = models.CharField(max_length=100)
    # Добавьте другие поля, представляющие клиента

    def __str__(self):
        return self.name

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class Order(models.Model):
    order_number = models.CharField(max_length=10, default='N/A')
    order_date = models.DateField(default=datetime.date.today)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return self.order_number
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.medication.name} ({self.quantity})'


class SellProductForm(forms.Form):
    search = forms.CharField(max_length=100)
    medication_id = forms.IntegerField()
    quantity = forms.IntegerField(min_value=1)


# Другие модели, например, для склада и поставок
