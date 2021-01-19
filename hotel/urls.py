from django.urls import path
from .views import ApartmentList, BookingList

app_name='hotel'

urlpatterns=[
    path('apartment_list', ApartmentList.as_view(), name='ApartmentList'),
    path('booking_list', BookingList.as_view(), name='BookingList'),
]