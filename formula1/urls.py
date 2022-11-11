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
    # Pilot
    path('pilots/', views.pilots_list, name='pilots_list'),
    path('pilots/search/', views.pilots_search, name='pilots_search'),
    path('pilots/<int:_id>/', views.pilots_get, name='pilots_get'),
    path('pilots/new/', views.pilots_new, name='pilots_new'),
    path('pilots/<int:_id>/edit/', views.pilots_edit, name='pilots_edit'),

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

    # Team
    path('teams/', views.teams_list, name='teams_list'),
    path('teams/search/', views.teams_search, name='teams_search'),
    path('teams/<int:_id>/', views.teams_get, name='teams_get'),
    path('teams/new/', views.teams_new, name='teams_new'),
    path('teams/<int:_id>/edit/', views.teams_edit, name='teams_edit'),
    # Team Leader
    path('teamleaders/', views.teamleaders_list, name='teamleaders_list'),
    path('teamleaders/search/', views.teamleaders_search, name='teamleaders_search'),
    path('teamleaders/<int:_id>/', views.teamleaders_get, name='teamleaders_get'),
    path('teamleaders/new/', views.teamleaders_new, name='teamleaders_new'),
    path('teamleaders/<int:_id>/edit/', views.teamleaders_edit, name='teamleaders_edit'),

    # Circuit
    path('circuits/', views.circuits_list, name='circuits_list'),
    path('circuits/search/', views.circuits_search, name='circuits_search'),
    path('circuits/<int:_id>/', views.circuits_get, name='circuits_get'),
    path('circuits/new/', views.circuits_new, name='circuits_new'),
    path('circuits/<int:_id>/edit/', views.circuits_edit, name='circuits_edit'),

    # Race
    path('races/', views.races_list, name='races_list'),
    path('races/search/', views.races_search, name='races_search'),
    path('races/<int:_id>/', views.races_get, name='races_get'),
    path('races/new/', views.races_new, name='races_new'),
    path('races/<int:_id>/edit/', views.races_edit, name='races_edit'),

    # Result
    path('results/', views.results_list, name='results_list'),
    path('results/search/', views.results_search, name='results_search'),
    path('results/<int:_id>/', views.results_get, name='results_get'),
    path('results/new/', views.results_new, name='results_new'),
    path('results/<int:_id>/edit/', views.results_edit, name='results_edit'),
]
