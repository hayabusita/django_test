from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {'message': 'This is message from context',
    'version': 123, 'objects': ['uno', 2]}
    return render(request, 'home.html', my_context)
