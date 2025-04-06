
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

]
