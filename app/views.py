from django.db.models import Q
from django.shortcuts import render, redirect

from app.models import Circuit, Race, Result, Team, TeamLeader, Pilot, Country, Car
from app.forms import PilotForm, PilotSearchForm, TeamForm, TeamSearchForm, TeamLeaderSearchForm, TeamLeaderForm, \
    CircuitSearchForm, CircuitForm, RaceSearchForm, RaceForm, ResultSearchForm, ResultForm, CountrySearchForm, \
    CountryForm, CarSearchForm, CarForm


# Create your views here.

def home(req):
    return render(req, 'home.html')


# Car

def cars_list(req):
    cars = Car.objects.all()
    actions = [{'str': 'Search Car', 'url': '/cars/search'},
               {'str': 'New Car', 'url': '/cars/new'}]
    lst = [[{'str': c.model, 'url': f'/cars/{c.id}'}] for c in cars]
    ctx = {'header': 'Cars', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def cars_new(req):
    if req.method == 'POST':
        form = CarForm(req.POST)
        if form.is_valid():
            Car.objects.create(
                model=form.cleaned_data['model'],
                engine=form.cleaned_data['engine'],
                weight=form.cleaned_data['weight'],
                pilot=form.cleaned_data['pilot']
            )

            return redirect('cars_list')
    else:
        form = CarForm()
        ctx = {'header': 'New Car', 'form': form}
        return render(req, 'new.html', ctx)


def cars_search(req):
    if req.method == 'POST':
        form = CarSearchForm(req.POST)
        if form.is_valid():
            model = form.cleaned_data['model']
            pilot = form.cleaned_data['pilot']
            cars = Car.objects.filter(Q(model__icontains=model)
                                      & Q(pilot__name__icontains=pilot))
            lst = [[{'str': c.model, 'url': f'/cars/{c.id}'}] for c in cars]

            query = f'Car.model={model};Car.pilot={pilot}'
            ctx = {'header': 'List of Cars', 'list': lst, 'query': query}
            return render(req, 'list.html', ctx)
    else:
        form = CarSearchForm()
        ctx = {'header': 'Search Car', 'form': form}
        return render(req, 'search.html', ctx)


def cars_get(req, _id):
    car = Car.objects.get(id=_id)

    ctx = {'header': 'Car Details', 'car': car}
    return render(req, 'car.html', ctx)


def cars_edit(req, _id):
    car = Car.objects.get(id=_id)
    if req.method == 'POST':
        form = CarForm(req.POST)
        if form.is_valid():
            car.model = form.cleaned_data['model']
            car.engine = form.cleaned_data['engine']
            car.weight = form.cleaned_data['weight']
            car.pilot = form.cleaned_data['pilot']
            car.save()

            return redirect('cars_get', _id=_id)
    else:
        form = CarForm(initial={
            'model': car.model,
            'engine': car.engine,
            'weight': car.weight,
            'pilot': car.pilot})
        ctx = {'header': 'Edit Car', 'form': form}
        return render(req, 'edit.html', ctx)


# Circuit

def circuits_list(req):
    circuits = Circuit.objects.all()
    actions = [{'str': 'Search Circuit', 'url': '/circuits/search'},
               {'str': 'New Circuit', 'url': '/circuits/new'}]
    lst = [[{'str': c.name, 'url': f'/circuits/{c.id}'}] for c in circuits]

    ctx = {'header': 'List of Circuits', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def circuits_search(req):
    # If POST request, process form data
    if req.method == 'POST':
        # Create a form instance and pass data to it
        form = CircuitSearchForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            query = f'Circuit.name={name}'
            # if 'searched' in req.session and req.session['searched'] == query:
            #     return HttpResponse('You have searched for the same thing before. Please try again.')
            # req.session['searched'] = query

            circuits = Circuit.objects.filter(name__icontains=name)

            lst = [[{'str': c.name, 'url': f'/circuits/{c.id}'}]
                   for c in circuits]
            ctx = {'header': 'List of Circuits', 'list': lst, 'query': query}
            return render(req, 'list.html', ctx)
    else:
        # If GET (or any other method), create blank form
        form = CircuitSearchForm()
        ctx = {'header': 'Search Circuit', 'form': form}
        return render(req, 'search.html', ctx)


def circuits_get(req, _id):
    circuit = Circuit.objects.get(id=_id)

    ctx = {'header': 'Circuit Details', 'circuit': circuit}
    return render(req, 'circuit.html', ctx)


def circuits_new(req):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    if req.method == 'POST':
        form = CircuitForm(req.POST)
        if form.is_valid():
            Circuit.objects.create(
                name=form.cleaned_data['name'],
                length=form.cleaned_data['length'],
                location=form.cleaned_data['location'],
                fast_lap=form.cleaned_data['fast_lap'],
                last_winner=form.cleaned_data['last_winner'],
                country=form.cleaned_data['country'],
            )

            return redirect('circuits_list')
    else:
        form = CircuitForm()
        ctx = {'header': 'New Circuit', 'form': form}
        return render(req, 'new.html', ctx)


def circuits_edit(req, _id):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    circuit = Circuit.objects.get(id=_id)
    if req.method == 'POST':
        form = CircuitForm(req.POST)
        if form.is_valid():
            circuit.name = form.cleaned_data['name']
            circuit.length = form.cleaned_data['length']
            circuit.location = form.cleaned_data['location']
            circuit.fast_lap = form.cleaned_data['fast_lap']
            circuit.last_winner = form.cleaned_data['last_winner']
            circuit.country = form.cleaned_data['country']
            circuit.save()

            return redirect('circuits_get', _id=_id)
    else:
        form = CircuitForm(initial={
            'name': circuit.name,
            'length': circuit.length,
            'location': circuit.location,
            'fast_lap': circuit.fast_lap,
            'last_winner': circuit.last_winner,
            'country': circuit.country.id
        })
        ctx = {'header': 'Edit Circuit', 'form': form}
        return render(req, 'edit.html', ctx)


# Country

def countries_list(req):
    countries = Country.objects.all()
    actions = [{'str': 'Search Country', 'url': '/countries/search'},
               {'str': 'New Country', 'url': '/countries/new'}]
    lst = [[{'str': c.designation, 'url': f'/countries/{c.id}'}] for c in countries]
    ctx = {'header': 'Countries', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def countries_get(req, _id):
    country = Country.objects.get(id=_id)

    ctx = {'header': 'Country Details', 'country': country}
    return render(req, 'country.html', ctx)


def countries_new(req):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    if req.method == 'POST':
        form = CountryForm(req.POST)
        if form.is_valid():
            Country.objects.create(
                designation=form.cleaned_data['designation'],
                code=form.cleaned_data['code']
            )

            return redirect('countries_list')
    else:
        form = CountryForm()
        ctx = {'header': 'New Country', 'form': form}
        return render(req, 'new.html', ctx)


def countries_search(req):
    if req.method == 'POST':
        form = CountrySearchForm(req.POST)
        if form.is_valid():
            designation = form.cleaned_data['designation']

            query = f'Country.designation={designation}'
            # if 'searched' in req.session and req.session['searched'] == query:
            #     return HttpResponse('You have searched for the same thing before. Please try again.')
            # req.session['searched'] = query

            countries = Country.objects.filter(designation__icontains=designation)

            lst = [[{'str': c.designation, 'url': f'/countries/{c.id}'}]
                   for c in countries]
            ctx = {'header': 'Countries', 'list': lst, 'query': query}
            return render(req, 'list.html', ctx)
    else:
        form = CountrySearchForm()
        ctx = {'header': 'Search Country', 'form': form}
        return render(req, 'search.html', ctx)


def countries_edit(req, _id):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    country = Country.objects.get(id=_id)
    if req.method == 'POST':
        form = CountryForm(req.POST)
        if form.is_valid():
            country.designation = form.cleaned_data['designation']
            country.code = form.cleaned_data['code']
            country.save()

            return redirect('countries_get', _id=_id)
    else:
        form = CountryForm(initial={
            'designation': country.designation,
            'code': country.code
        })
        ctx = {'header': 'Edit Country', 'form': form}
        return render(req, 'edit.html', ctx)


# Pilot

def pilots_list(req):
    pilots = Pilot.objects.all()
    actions = [{'str': 'Search Pilot', 'url': '/pilots/search'},
               {'str': 'New Pilot', 'url': '/pilots/new'}]
    lst = [[{'str': p.name, 'url': f'/pilots/{p.id}'}] for p in pilots]

    ctx = {'header': 'List of Pilots', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def pilots_search(req):
    # If POST request, process form data
    if req.method == 'POST':
        # Create a form instance and pass data to it
        form = PilotSearchForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            query = f'Pilot.name={name}'
            # if 'searched' in req.session and req.session['searched'] == query:
            #     return HttpResponse('You have searched for the same thing before. Please try again.')
            # req.session['searched'] = query

            pilots = Pilot.objects.filter(name__icontains=name)

            lst = [[{'str': p.name, 'url': f'/pilots/{p.id}'}]
                   for p in pilots]
            ctx = {'header': 'List of Pilots', 'list': lst, 'query': query}
            return render(req, 'list.html', ctx)
    else:
        # If GET (or any other method), create blank form
        form = PilotSearchForm()
        ctx = {'header': 'Search Pilot', 'form': form}
        return render(req, 'search.html', ctx)


def pilots_get(req, _id):
    pilot = Pilot.objects.get(id=_id)

    ctx = {'header': 'Pilot Details', 'pilot': pilot}
    return render(req, 'pilot.html', ctx)


def pilots_new(req):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    if req.method == 'POST':
        form = PilotForm(req.POST)
        if form.is_valid():
            pilot = Pilot.objects.create(
                name=form.cleaned_data['name'],
                date=form.cleaned_data['date'],
                victories=form.cleaned_data['victories'],
                pole_positions=form.cleaned_data['pole_positions'],
                podiums=form.cleaned_data['podiums'],
                championships=form.cleaned_data['championships'],
                contract=form.cleaned_data['contract'],
                entry_year=form.cleaned_data['entry_year'],
                team=form.cleaned_data['team'],
                team_leader=form.cleaned_data['team_leader'],
            )
            pilot.country.set(form.cleaned_data['country'])

            return redirect('pilots_list')
    else:
        form = PilotForm()
        ctx = {'header': 'New Pilot', 'form': form}
        return render(req, 'new.html', ctx)


def pilots_edit(req, _id):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    pilot = Pilot.objects.get(id=_id)
    if req.method == 'POST':
        form = PilotForm(req.POST)
        if form.is_valid():
            pilot.name = form.cleaned_data['name']
            pilot.date = form.cleaned_data['date']
            pilot.victories = form.cleaned_data['victories']
            pilot.pole_positions = form.cleaned_data['pole_positions']
            pilot.podiums = form.cleaned_data['podiums']
            pilot.championships = form.cleaned_data['championships']
            pilot.contract = form.cleaned_data['contract']
            pilot.entry_year = form.cleaned_data['entry_year']
            pilot.team = form.cleaned_data['team']
            pilot.country.set(form.cleaned_data['country'])
            pilot.save()

            return redirect('pilots_get', _id=_id)
    else:
        form = PilotForm(initial={
            'name': pilot.name,
            'date': pilot.date,
            'victories': pilot.victories,
            'pole_positions': pilot.pole_positions,
            'podiums': pilot.podiums,
            'championships': pilot.championships,
            'contract': pilot.contract,
            'entry_year': pilot.entry_year,
            'team': pilot.team.id,
            'country': [c.id for c in pilot.country.all()]
        })
        ctx = {'header': 'Edit Pilot', 'form': form}
        return render(req, 'edit.html', ctx)


# Race

def races_list(req):
    races = Race.objects.all()
    actions = [{'str': 'Search Race', 'url': '/races/search'},
               {'str': 'New Race', 'url': '/races/new'}]
    lst = [[{'str': r.name, 'url': f'/races/{r.id}'}] for r in races]

    ctx = {'header': 'List of Races', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def races_search(req):
    # If POST request, process form data
    if req.method == 'POST':
        # Create a form instance and pass data to it
        form = RaceSearchForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            query = f'Race.name={name}'
            # if 'searched' in req.session and req.session['searched'] == query:
            #     return HttpResponse('You have searched for the same thing before. Please try again.')
            # req.session['searched'] = query

            races = Race.objects.filter(name__icontains=name)

            lst = [[{'str': r.name, 'url': f'/races/{r.id}'}]
                   for r in races]
            ctx = {'header': 'List of Races', 'list': lst, 'query': query}
            return render(req, 'list.html', ctx)
    else:
        # If GET (or any other method), create blank form
        form = RaceSearchForm()
        ctx = {'header': 'Search Race', 'form': form}
        return render(req, 'search.html', ctx)


def races_get(req, _id):
    race = Race.objects.get(id=_id)

    ctx = {'header': 'Race Details', 'race': race}
    return render(req, 'race.html', ctx)


def races_new(req):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    if req.method == 'POST':
        form = RaceForm(req.POST)
        if form.is_valid():
            Race.objects.create(
                name=form.cleaned_data['name'],
                date=form.cleaned_data['date'],
                season=form.cleaned_data['season'],
                circuit=form.cleaned_data['circuit'],
            )

            return redirect('races_list')
    else:
        form = RaceForm()
        ctx = {'header': 'New Race', 'form': form}
        return render(req, 'new.html', ctx)


def races_edit(req, _id):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    race = Race.objects.get(id=_id)
    if req.method == 'POST':
        form = RaceForm(req.POST)
        if form.is_valid():
            race.name = form.cleaned_data['name']
            race.date = form.cleaned_data['date']
            race.season = form.cleaned_data['season']
            race.circuit = form.cleaned_data['circuit']
            race.save()

            return redirect('races_get', _id=_id)
    else:
        form = RaceForm(initial={
            'name': race.name,
            'date': race.date,
            'season': race.season,
            'circuit': race.circuit.id
        })
        ctx = {'header': 'Edit Race', 'form': form}
        return render(req, 'edit.html', ctx)


# Result

def results_list(req):
    results = Result.objects.all()
    actions = [{'str': 'Search Result', 'url': '/results/search'},
               {'str': 'New Result', 'url': '/results/new'}]
    lst = [[{'str': r.pilot, 'url': f'/results/{r.id}'}] for r in results]

    ctx = {'header': 'List of Results', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def results_search(req):
    # If POST request, process form data
    if req.method == 'POST':
        # Create a form instance and pass data to it
        form = ResultSearchForm(req.POST)
        if form.is_valid():
            pilot = form.cleaned_data['pilot']
            race = form.cleaned_data['race']

            query = f'Result.pilot={pilot};Result.race={race}'
            # if 'searched' in req.session and req.session['searched'] == query:
            #     return HttpResponse('You have searched for the same thing before. Please try again.')
            # req.session['searched'] = query

            result = Result.objects.filter(Q(pilot=pilot) & Q(race=race))

            return redirect('results_get', _id=result[0].id)
    else:
        # If GET (or any other method), create blank form
        form = ResultSearchForm()
        ctx = {'header': 'Search Result', 'form': form}
        return render(req, 'search.html', ctx)


def results_get(req, _id):
    result = Result.objects.get(id=_id)

    ctx = {'header': 'Result Details', 'result': result}
    return render(req, 'result.html', ctx)


def results_new(req):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    if req.method == 'POST':
        form = ResultForm(req.POST)
        if form.is_valid():
            Result.objects.create(
                position=form.cleaned_data['position'],
                pilot=form.cleaned_data['pilot'],
                race=form.cleaned['race'],
                points=form.cleaned_data['points']
            )

            return redirect('results_list')
    else:
        form = ResultForm()
        ctx = {'header': 'New Result', 'form': form}
        return render(req, 'new.html', ctx)


def results_edit(req, _id):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    result = Result.objects.get(id=_id)
    if req.method == 'POST':
        form = ResultForm(req.POST)
        if form.is_valid():
            result.position = form.cleaned_data['position']
            result.pilot = form.cleaned_data['pilot']
            result.race = form.cleaned_data['race']
            result.points = form.cleaned_data['points']
            result.save()

            return redirect('results_get', _id=_id)
    else:
        form = ResultForm(initial={
            'position': result.position,
            'pilot': result.pilot,
            'race': result.race,
            'points': result.points
        })
        ctx = {'header': 'Edit Result', 'form': form}
        return render(req, 'edit.html', ctx)


# Team

def teams_list(req):
    teams = Team.objects.all()
    actions = [{'str': 'Search Team', 'url': '/teams/search'},
               {'str': 'New Team', 'url': '/teams/new'}]
    lst = [[{'str': t.name, 'url': f'/teams/{t.id}'}] for t in teams]

    ctx = {'header': 'List of Teams', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def teams_search(req):
    # If POST request, process form data
    if req.method == 'POST':
        # Create a form instance and pass data to it
        form = TeamSearchForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            query = f'Team.name={name}'
            # if 'searched' in req.session and req.session['searched'] == query:
            #     return HttpResponse('You have searched for the same thing before. Please try again.')
            # req.session['searched'] = query

            teams = Team.objects.filter(name__icontains=name)

            lst = [[{'str': t.name, 'url': f'/teams/{t.id}'}]
                   for t in teams]
            ctx = {'header': 'List of Teams', 'list': lst, 'query': query}
            return render(req, 'list.html', ctx)
    else:
        # If GET (or any other method), create blank form
        form = TeamSearchForm()
        ctx = {'header': 'Search Team', 'form': form}
        return render(req, 'search.html', ctx)


def teams_get(req, _id):
    team = Team.objects.get(id=_id)

    ctx = {'header': 'Team Details', 'team': team}
    return render(req, 'team.html', ctx)


def teams_new(req):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    if req.method == 'POST':
        form = TeamForm(req.POST)
        if form.is_valid():
            Team.objects.create(
                name=form.cleaned_data['name'],
                date=form.cleaned_data['date'],
                championships=form.cleaned_data['championships']
            )

            return redirect('teams_list')
    else:
        form = TeamForm()
        ctx = {'header': 'New Team', 'form': form}
        return render(req, 'new.html', ctx)


def teams_edit(req, _id):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    team = Team.objects.get(id=_id)
    if req.method == 'POST':
        form = TeamForm(req.POST)
        if form.is_valid():
            team.name = form.cleaned_data['name']
            team.date = form.cleaned_data['date']
            team.championships = form.cleaned_data['championships']
            team.save()

            return redirect('teams_get', _id=_id)
    else:
        form = TeamForm(initial={
            'name': team.name,
            'date': team.date,
            'championships': team.championships
        })
        ctx = {'header': 'Edit Team', 'form': form}
        return render(req, 'edit.html', ctx)


# TeamLeader

def teamleaders_list(req):
    teamleaders = TeamLeader.objects.all()
    actions = [{'str': 'Search Team Leader', 'url': '/teamleaders/search'},
               {'str': 'New Team Leader', 'url': '/teamleaders/new'}]
    lst = [[{'str': tl.name, 'url': f'/teamleaders/{tl.id}'}] for tl in teamleaders]

    ctx = {'header': 'List of Team Leaders', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def teamleaders_search(req):
    # If POST request, process form data
    if req.method == 'POST':
        # Create a form instance and pass data to it
        form = TeamLeaderSearchForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            query = f'TeamLeader.name={name}'
            # if 'searched' in req.session and req.session['searched'] == query:
            #     return HttpResponse('You have searched for the same thing before. Please try again.')
            # req.session['searched'] = query

            teamleaders = TeamLeader.objects.filter(name__icontains=name)

            lst = [[{'str': tl.name, 'url': f'/teams/{tl.id}'}]
                   for tl in teamleaders]
            ctx = {'header': 'List of Team Leaders', 'list': lst, 'query': query}
            return render(req, 'list.html', ctx)
    else:
        # If GET (or any other method), create blank form
        form = TeamLeaderSearchForm()
        ctx = {'header': 'Search Team Leader', 'form': form}
        return render(req, 'search.html', ctx)


def teamleaders_get(req, _id):
    teamleader = TeamLeader.objects.get(id=_id)

    ctx = {'header': 'Team Leader Details', 'teamleader': teamleader}
    return render(req, 'teamleader.html', ctx)


def teamleaders_new(req):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    if req.method == 'POST':
        form = TeamLeaderForm(req.POST)
        if form.is_valid():
            Team.objects.create(
                name=form.cleaned_data['name'],
                team=form.cleaned_data['team']
            )

            return redirect('teamleaders_list')
    else:
        form = TeamLeaderForm()
        ctx = {'header': 'New Team Leader', 'form': form}
        return render(req, 'new.html', ctx)


def teamleaders_edit(req, _id):
    if not req.user.is_authenticated or req.user.username != 'admin':
        return redirect('login')
    teamleader = TeamLeader.objects.get(id=_id)
    if req.method == 'POST':
        form = TeamLeaderForm(req.POST)
        if form.is_valid():
            teamleader.name = form.cleaned_data['name']
            teamleader.team = form.cleaned_data['team']
            teamleader.save()

            return redirect('teamleaders_get', _id=_id)
    else:
        form = TeamLeaderForm(initial={
            'name': teamleader.name,
            'team': teamleader.team.id
        })
        ctx = {'header': 'Edit Team Leader', 'form': form}
        return render(req, 'edit.html', ctx)
