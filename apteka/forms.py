from django import forms
from .models import *

class SearchForm(forms.Form):
    medication_id = forms.IntegerField(label='ID товара', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='Количество', widget=forms.NumberInput(attrs={'class': 'form-control'}))

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'order_date', 'customer', 'items', 'total_amount']
        
    items = forms.ModelMultipleChoiceField(queryset=Medication.objects.all())

class SellProductFormSet(forms.Form):
    medication_id = forms.IntegerField(label='ID товара', required=False)
    medication_name = forms.CharField(label='Название товара', required=False)
    quantity = forms.IntegerField(label='Количество', min_value=1)