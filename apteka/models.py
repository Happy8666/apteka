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
    numberPhone = models.CharField(max_length=100)
    # Другие поля для клиента

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class Order(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Другие поля для заказа


class SellProductForm(forms.Form):
    search = forms.CharField(max_length=100)
    medication_id = forms.IntegerField()
    quantity = forms.IntegerField(min_value=1)


# Другие модели, например, для склада и поставок
