"""formula1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from app import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Home
    path('', views.home, name='home'),
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # Drivers
    path('drivers/', views.drivers_list, name='drivers_list'),
    # Teams
    path('teams/', views.teams_list, name='teams_list'),
    #Country
    path('countries/', views.country_list, name='country_list'),
    path('countries/new/', views.country_new, name='country_new'),
    path('countries/search/', views.country_search, name='country_search'),
    path('countries/<str:code>/', views.country_get, name='country_get'),
    path('countries/<str:code>/edit/', views.country_edit, name='country_edit'),

    #Car
    path('cars/', views.car_list, name='car_list'),
    path('cars/new/', views.car_new, name='car_new'),
    path('cars/search/', views.car_search, name='car_search'),
    path('cars/<str:model>/', views.car_get, name='car_get'),
    path('cars/<str:model>/edit/', views.car_edit, name='car_edit'),
]
