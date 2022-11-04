from django.shortcuts import render, redirect


# Create your views here.

def home(req):
    return render(req, 'home.html')

# Drivers

def drivers_list(req):
    return redirect('home')

# Teams

def teams_list(req):
    return redirect('home')