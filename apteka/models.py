from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.name
    # Другие поля для лекарства

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # Другие поля для клиента

class Order(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Другие поля для заказа


# Другие модели, например, для склада и поставок
