from django.shortcuts import render
from django.views.generic import ListView
from .models import Apartment, Booking

# Create your views here.

class ApartmentList(ListView):
    model=Apartment

class BookingList(ListView):
    model=Booking