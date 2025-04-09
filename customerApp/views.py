from django.shortcuts import render

# Create your views here.
def Cust_dashboard(request):
    return render(request , 'index.html' ,{})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Service
def register_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('Cust_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')
def services_list(request):
    services = Service.objects.all().order_by('category', 'name')
    return render(request, 'services.html', {'services': services})
#@login_required
#@user_passes_test(lambda u: u.is_superuser)
#def admin_dashboard(request):
  #  return render(request, 'admin_dashboard.html')

#@login_required
#@user_passes_test(lambda u: not u.is_superuser)
#def customer_dashboard(request):
 #   return render(request, 'customer_dashboard.html')

def contact(request):
    return render(request,'contact.html' ,{})
