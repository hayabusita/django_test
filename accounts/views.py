from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not  None:
            login(request, user)    # request.user == user
            return redirect('/')
        else:
            # attempt = request.session['attempt'] or 0
            # request.session['attempt'] = attempt + 1
            # return redirect('/invalid-password')
            request.session['invalid_user'] = 1

    return render(request, 'register_login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        try:
            user = User.objects.create_user(username, email, password1)
        except:
            user = None

        if user is not  None:
            login(request, user)    # request.user == user
            return redirect('/')
        else:
            request.session['register_error'] = 1

    return render(request, 'register_login.html', {'form': form})