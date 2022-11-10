from django import forms

from app.models import Pilot, Country, Team


# Create your forms here.

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