from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def products_detailed_view(request):
    obj = Product.objects.all()
    context = {'objects': obj}
    return render(request, 'products/detail.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)