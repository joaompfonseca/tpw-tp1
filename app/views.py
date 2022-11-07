from django.shortcuts import render, redirect
from models import Circuit, Race, Result

# Create your views here.

def home(req):
    return render(req, 'home.html')

# Drivers

def drivers_list(req):
    return redirect('home')

# Teams

def teams_list(req):
    return redirect('home')


# - Circuit
def circuit_list(req):
    circuit_qs = Circuit.objects.all()
    circuits_list = []
    for circuit in circuit_qs:
        circuits_list.append(str(circuit))
    return circuits_list


def update_circuit(req, circuit, name=None, length=None, location=None, fast_lap=None, last_winner=None, country=None):
    if name is not None:
        circuit.name = name
    if length is not None:
        circuit.length = length
    if location is not None:
        circuit.location = location
    if fast_lap is not None:
        circuit.fast_lap = fast_lap
    if last_winner is not None:
        circuit.last_winner = last_winner
    if country is not None:
        circuit.country = country
    return circuit.save()


def new_circuit(req, name=None, length=None, location=None, fast_lap=None, last_winner=None, country=None):
    circuit = Circuit(name, length, location, fast_lap, last_winner, country)
    return circuit.save()
