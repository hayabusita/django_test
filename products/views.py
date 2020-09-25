from django.shortcuts import render
from .models import Product

# Create your views here.
def products_detailed_view(request):
    obj = Product.objects.all()
    context = {'objects': obj}
    return render(request, 'products/detail.html', context)