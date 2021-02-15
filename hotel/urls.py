from django.urls import path
from .views import index, BookingList, ApartmentDetail, CancelBooking, CalendarView
from django.conf.urls.static import static
from django.conf import settings

app_name='hotel'

urlpatterns=[
    path('index', index, name='index'),
    path('booking_list', BookingList.as_view(), name='BookingList'),
    path('apartment/<category>', ApartmentDetail.as_view(), name='ApartmentDetail'),
    path('booking/cancel/<pk>', CancelBooking.as_view(), name='CancelBooking'),
    path('calendar/', CalendarView.as_view(), name='calendar'),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)