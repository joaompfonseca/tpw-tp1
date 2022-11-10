from django.db import models

# Create your models here.

class Country(models.Model):
    designation = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    def __str__(self):
        return self.designation
class Team(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateField()
    championships = models.IntegerField()
    def __str__(self):
        return self.name

class TeamLeader(models.Model):
    name = models.CharField(max_length=70)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Pilot(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateField()
    victories = models.IntegerField()
    pole_positions = models.IntegerField()
    podiums = models.IntegerField()
    championships = models.IntegerField()
    contract = models.IntegerField()
    entry_year = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    country = models.ManyToManyField(Country)
    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=70)
    engine = models.CharField(max_length=70)
    weight = models.IntegerField()
    pilot = models.OneToOneField(Pilot, on_delete=models.CASCADE)
    def __str__(self):
        return self.model

class Circuit(models.Model):
    name = models.CharField(max_length=70)
    length = models.IntegerField()
    location = models.CharField(max_length=70)
    fast_lap = models.TimeField()
    last_winner = models.OneToOneField(Pilot, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateField()
    season = models.IntegerField()
    circuit = models.OneToOneField(Circuit, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Result(models.Model):
    position = models.IntegerField()
    pilot = models.OneToOneField(Pilot, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return self.position