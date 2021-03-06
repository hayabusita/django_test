from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
#from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import JsonResponse

# Create your views here.
def api_products_detailed_view(request):
    queryset = Product.objects.all()
    json_array = []
    for product in queryset:
        json_array.append({
            "name": product.name,
            "description": product.description,
            "price": float(product.price)
            })

    return JsonResponse(json_array, safe=False)

def products_detailed_view(request):
    obj = Product.objects.all()
    context = {'objects': obj}
    return render(request, 'products/detail.html', context)

# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
            
#     context = {'form': form}
#     return render(request, 'products/product_create.html', context)

#def product_create_view(request):
#    if request.method == 'POST':
#        new_name = request.POST.get('name')
#        print(new_name)
#
#    context = {}
#    return render(request, 'products/product_create.html', context)

@staff_member_required
def product_create_view(request):
    form = ProductForm(request.POST or None)
   
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ProductForm()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)

def product_update_view(request, prod_id):
    obj = get_object_or_404(Product, id=prod_id)
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
    
    context = {'form': form}
    return render(request, "products/product_create.html", context)

def product_view(request, prod_id):
    #obj = Product.objects.get(id=prod_id)
    obj = get_object_or_404(Product, id=prod_id)
    context = {'object': obj}

    return render(request, 'products/product.html', context)

def product_delete_view(request, prod_id):
    obj = get_object_or_404(Product, id=prod_id)

    if request.method == 'POST':
        obj.delete()
        return redirect(products_detailed_view)

    context = {'object': obj}
    
    return render(request, 'products/product_delete.html', context)