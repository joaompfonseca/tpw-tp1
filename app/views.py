from django.shortcuts import render, redirect

from app.models import Circuit, Race, Result, Team, TeamLeader, Pilot
from app.forms import PilotForm, PilotSearchForm, TeamForm, TeamSearchForm, TeamLeaderSearchForm, TeamLeaderForm


# Create your views here.

def home(req):
    return render(req, 'home.html')


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


# - Circuit
def circuit_list(req):
    circuits = Team.objects.all()
    actions = [{'str': 'Search Circuit', 'url': '/teams/search'},
               {'str': 'New Circuit', 'url': '/teams/new'}]
    lst = [[{'str': c.name, 'url': f'/teams/{c.id}', 'length': c.length,
             'location': c.location, 'fast_lap': c.fast_lap, 'last_winner': c.last_winner}] for c in circuits]

    ctx = {'header': 'List of Teams', 'actions': actions, 'list': lst}
    return render(req, 'list.html', ctx)


def circuit_search(req):
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


def circuit_get(req, _id):
    team = Team.objects.get(id=_id)

    ctx = {'header': 'Team Details', 'team': team}
    return render(req, 'team.html', ctx)


def circuit_new(req):
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


def circuit_edit(req, _id):
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

