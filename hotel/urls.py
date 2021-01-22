from django.urls import path
from .views import ApartmentList, BookingList, ApartmentDetail, CancelBooking
from django.conf.urls.static import static
from django.conf import settings

app_name='hotel'

urlpatterns=[
    path('apartment_list', ApartmentList, name='ApartmentList'),
    path('booking_list', BookingList.as_view(), name='BookingList'),
    path('apartment/<category>', ApartmentDetail.as_view(), name='ApartmentDetail'),
    path('booking/cancel/<pk>', CancelBooking.as_view(), name='CancelBooking')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)