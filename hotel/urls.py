from django.urls import path
from .views import ApartmentList, BookingList, BookingView, ApartmentDetail

app_name='hotel'

urlpatterns=[
    path('apartment_list', ApartmentList, name='ApartmentList'),
    path('booking_list', BookingList.as_view(), name='BookingList'),
    path('book', BookingView.as_view(), name='BookingView'),
    path('apartment/<category>', ApartmentDetail.as_view(), name='ApartmentDetail'),

]