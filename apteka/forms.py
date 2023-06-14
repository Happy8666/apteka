from django import forms

class SearchForm(forms.Form):
    medication_id = forms.IntegerField(label='ID товара', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='Количество', widget=forms.NumberInput(attrs={'class': 'form-control'}))
