from django.shortcuts import render

# Create your views here.
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.object.all()
    })

def flight(request, flight_id):
	flight = Flight.object.get(pk=flight_id)
	return render(request, "flights/flight.html", {
          "flight": flight, 
          "passengers": flight.passengers.all(),
          "non_passenger": Passenger.objects.exclude(flights=flight).all()})

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.object.get(pk=flight_id)
        passenger = Passenger.objects.get(int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id)))