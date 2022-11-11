from django import forms

from app.models import Country, Car, Pilot, Country, Team, Circuit, Race


# Create your forms here.

# Country
class CountryForm(forms.Form):
    designation = forms.CharField(label='Name:', max_length=50, required=True)
    code = forms.CharField(label='Code:', max_length=3, required=True)

class CountrySearchForm(forms.Form):
    code = forms.CharField(label='Code:', max_length=3)

class CarForm(forms.Form):
    model = forms.CharField(label='Model:', max_length=70, required=True)
    engine = forms.CharField(label='Engine:', max_length=70, required=True)
    weight = forms.IntegerField(label='Weight:', required=True)
    pilot = forms.ModelChoiceField(label='Pilot:', queryset=Pilot.objects.all(), required=True)

class CarSearchForm(forms.Form):
    model = forms.CharField(label='Model:', max_length=70,required=False)
    pilot = forms.CharField(label='Pilot:', max_length=70, required=False)

# Pilot

class PilotForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    date = forms.DateField(label='Date of Birth:')
    victories = forms.IntegerField(label='Victories:')
    pole_positions = forms.IntegerField(label='Pole Positions:')
    podiums = forms.IntegerField(label='Podiums:')
    championships = forms.IntegerField(label='Championships:')
    contract = forms.IntegerField(label='Contract:')
    entry_year = forms.IntegerField(label='Entry Year:')
    team = forms.ModelChoiceField(label='Team:', queryset=Team.objects.all())
    country = forms.ModelMultipleChoiceField(label='Country:', queryset=Country.objects.all())

class PilotSearchForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)

# Team

class TeamForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    date = forms.DateField(label='Fundation Date:')
    championships = forms.IntegerField(label='Championships:')

class TeamSearchForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)


# TeamLeader

class TeamLeaderForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    team = forms.ModelChoiceField(label='Team:', queryset=Team.objects.all())


class TeamLeaderSearchForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)


class CircuitSearchForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)


class CircuitForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    length = forms.IntegerField(label='Length:')
    location = forms.CharField(label='Location:', max_length=70)
    fast_lap = forms.TimeField(label='Fast Lap:')
    last_winner = forms.ModelChoiceField(label='Last Winner:', queryset=Pilot.objects.all())
    country = forms.ModelChoiceField(label='Country:', queryset=Country.objects.all())


class RaceForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    date = forms.DateField(label='Date:')
    season = forms.IntegerField(label='Season:')
    circuit = forms.ModelChoiceField(label='Circuit:', queryset=Circuit.objects.all())


class RaceSearchForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)


class ResultForm(forms.Form):
    position = forms.IntegerField(label='Position:')
    pilot = forms.ModelChoiceField(label='Pilot:', queryset=Pilot.objects.all())
    race = forms.ModelChoiceField(label='Race:', queryset=Race.objects.all())
    points = forms.IntegerField(label='Points:')


class ResultSearchForm(forms.Form):
    pilot = forms.ModelChoiceField(label='Pilot:', queryset=Pilot.objects.all())
    race = forms.ModelChoiceField(label='Race:', queryset=Race.objects.all())
