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
]
