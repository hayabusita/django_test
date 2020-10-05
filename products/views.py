from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def products_detailed_view(request):
    obj = Product.objects.all()
    context = {'objects': obj}
    return render(request, 'products/detail.html', context)

def product_create_view(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
            
    context = {'form': form}
    return render(request, 'products/product_create.html', context)

#def product_create_view(request):
#    if request.method == 'POST':
#        new_name = request.POST.get('name')
#        print(new_name)
#
#    context = {}
#    return render(request, 'products/product_create.html', context)

#def product_create_view(request):
#    form = ProductForm(request.POST or None)
#    
#    if form.is_valid():
#        form.save()
#        form = ProductForm()
#
#    context = {'form': form}
#    return render(request, 'products/product_create.html', context)