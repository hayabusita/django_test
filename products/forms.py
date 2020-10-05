from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class RawProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()