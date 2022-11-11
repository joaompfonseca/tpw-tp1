from django.contrib import admin
from app.models import Country, Team, TeamLeader, Pilot, Car, Circuit, Race, Result

# Register your models here.
admin.site.register(Country)
admin.site.register(Team)
admin.site.register(TeamLeader)
admin.site.register(Pilot)
admin.site.register(Car)
admin.site.register(Circuit)
admin.site.register(Race)
admin.site.register(Result)
