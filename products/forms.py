from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class RawProductForm(forms.Form):
    name = forms.CharField(
        label='', 
        widget=forms.TextInput( 
            attrs={'placeholder': 'Product name'}
            )
        )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Short description',
                'class': 'class-name-one class-name-two',
                'id': 'description-area',
                'rows': 15,
                'cols': 30
                }
            )
        )
    price = forms.DecimalField(initial=19.99)