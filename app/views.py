from django.db.models import Q
from django.shortcuts import render, redirect
from app.models import Country, Team, TeamLeader, Pilot, Car, Circuit, Race, Result
from app.forms import CountryForm, CountrySearchForm, CarForm, CarSearchForm

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

## Country

def country_list(req):
    countries = Country.objects.all()
    actions = [{'str': 'Search Country', 'url': '/countries/search'},
               {'str': 'New Country', 'url': '/countries/new'}]
    lst = [[{'str': c.designation, 'url': f'/countries/{c.code}'}] for c in countries]
    ctx = {'header': 'Countries', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)

def country_get(req, code):
    country = Country.objects.get(code=code)

    ctx = {'header': 'Country Details', 'country': country}
    return render(req, 'country.html', ctx)

def country_new(req):
    if req.method == 'POST':
        form = CountryForm(req.POST)
        if form.is_valid():
            designation = form.cleaned_data['designation']
            code = form.cleaned_data['code']
            country = Country.objects.create(designation=designation, code=code)
            return redirect('country_list')
    else:
        form = CountryForm()
        ctx = {'header': 'New Country', 'form': form}
        return render(req, 'new.html', ctx)

def country_search(request):
    if request.method == 'POST':
        form = CountrySearchForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            countries = Country.objects.filter(Q(code__icontains=code))
            lst = [[{'str': c.designation, 'url': f'/countries/{c.code}'}] for c in countries]
            query = f'code={code}'
            ctx = {'header': 'Countries', 'list': lst, 'query': query}
            return render(request, 'list.html', ctx)
    else:
        form = CountrySearchForm()
        ctx = {'header': 'Search Country', 'form': form}
        return render(request, 'search.html', ctx)

def country_edit(req,code):
    country = Country.objects.get(code=code)
    if req.method == 'POST':
        form = CountryForm(req.POST)
        if form.is_valid():
            designation = form.cleaned_data['designation']
            code = form.cleaned_data['code']

            country.designation = designation
            country.code = code
            country.save()

            return redirect('country_list')
    else:
        form = CountryForm(initial={'designation': country.designation, 'code': country.code})
        ctx = {'header': 'Edit Country', 'form': form}
        return render(req, 'edit.html', ctx)

def car_list(req):
    cars = Car.objects.all()
    actions = [{'str': 'Search Car', 'url': '/cars/search'},
               {'str': 'New Car', 'url': '/cars/new'}]
    lst = [[{'str': c.model, 'url': f'/cars/{c.model}'}] for c in cars]
    ctx = {'header': 'Cars', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def car_new(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data['model']
            engine = form.cleaned_data['engine']
            weight = form.cleaned_data['weight']
            pilot = form.cleaned_data['pilot']

            car = Car.objects.create(model=model, engine=engine, weight=weight, pilot=pilot)

            return redirect('car_list')

    else:
        form = CarForm()
        ctx = {'header': 'New Car', 'form': form}
        return render(request, 'new.html', ctx)


def car_search(request):
    if request.method == 'POST':
        form = CarSearchForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data['model']
            pilot = form.cleaned_data['pilot']
            cars = Car.objects.filter(Q(model__icontains=model)
                                      & Q(pilot__name__icontains=pilot))
            lst = [[{'str': c.model, 'url': f'/cars/{c.model}'}] for c in cars]

            query = f'model={model};pilot={pilot}'
            ctx = {'header': 'List of Cars', 'list': lst, 'query': query}
            return render(request, 'list.html', ctx)
    else:
        form = CarSearchForm()
        ctx = {'header': 'Search Car', 'form': form}
        return render(request, 'search.html', ctx)


def car_get(req, model):
    car = Car.objects.get(model=model)
    ctx = {'header': 'Car Details', 'car': car}
    return render(req, 'car.html', ctx)


def car_edit(request,model):
    car = Car.objects.get(model=model)
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data['model']
            engine = form.cleaned_data['engine']
            weight = form.cleaned_data['weight']
            pilot = form.cleaned_data['pilot']

            car.model = model
            car.engine = engine
            car.weight = weight
            car.pilot = pilot
            car.save()

            return redirect('car_list')
    else:
        form = CarForm(initial={'model': car.model, 'engine': car.engine, 'weight': car.weight, 'pilot': car.pilot})
        ctx = {'header': 'Edit Car', 'form': form}
        return render(request, 'edit.html', ctx)
