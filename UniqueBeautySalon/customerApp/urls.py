
from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.Cust_dashboard, name='index'),
    path('' ,views.Cust_dashboard ,name="Cust_dashboard"),
    path('register/', views.register_customer, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('services/', views.services_list, name='services'),
    path('contact/', views.contact, name='contact'),
    path('book/<int:package_id>/', views.book_package, name='book'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('make_package/', views.make_package, name='make_package'),
    path('blog/', views.blog, name='blog'),
]
