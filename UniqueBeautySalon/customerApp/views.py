from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Service , Package , Booking

# Create your views here.


def Cust_dashboard(request):
    packages = Package.objects.all()
    def group_packages(packages, n=2):
        return [packages[i:i+n] for i in range(0, len(packages), n)]

    grouped_packages = group_packages(list(packages))

    return render(request, 'index.html', {
        'grouped_packages': grouped_packages
    })


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

def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        booking = Booking.objects.create(
            package=package,
            customer_name=customer_name,
            date=date,
            time=time
        )
        request.session['booking_id'] = booking.id
        return redirect('booking_confirmation')

    return render(request, 'book_package.html', {'package': package})

def booking_confirmation(request):
    booking_id = request.session.get('booking_id')
    booking = Booking.objects.get(id=booking_id) if booking_id else None
    return render(request, 'booking-confirmation.html', {'booking': booking})

def make_package(request):
    return render(request,'makepackage.html' ,{})


def blog(request):
    return render(request, 'blog.html' ,{})
