from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, Passenger

class PassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("flights",)
	
admin.site.register(Passenger, PassengerAdmin)
	
class FlightAdmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")
	
admin.site.register(Flight, FlightAdmin)

admin.site.register(Airport)

