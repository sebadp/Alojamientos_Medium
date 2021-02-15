import datetime
from django.utils import timezone 
from hotel.models import Apartment, Booking 

def check_availability(apartment, check_in, check_out):

    avail_list=[]
    booking_list= Booking.objects.filter(apartment=apartment)
    for booking in booking_list:
        if booking.check_in>check_out or booking.check_out<check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
    
# def check_reality():
    