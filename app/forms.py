from django import forms

from app.models import Country, Car, Pilot


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