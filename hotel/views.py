from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from .models import Apartment, Booking
from .forms import AvailabilityForm
from django.utils import timezone
import datetime
from django.utils.safestring import mark_safe
from hotel.booking_functions.availability import check_availability
from django.urls import reverse_lazy,reverse
# Create your views here.

# class ApartmentList(ListView):
#     model=Apartment

def index(request):
    apartments= Apartment.objects.all()#[0]
#     apartment_categories = dict(apartment.APARTMENT_CATEGORIES)
#     # print('categories', apartment_categories)
#     apartment_values= apartment_categories.values()
#     # print('values', apartment_values)
#     apartment_list=[]
#     for apartment_category in apartment_categories:
#         apartment= apartment_categories.get(apartment_category)
#         apartment_url= reverse('hotel:ApartmentDetail', kwargs={'category': apartment_category})
#         apartment_list.append((apartment, apartment_url, apartment_description))



#    context={'apartment_list': apartment_list}
#    return render(request, 'apartment_list.html', context)
    context= {
        'apartments': apartments,
    }
    return render(request, 'hotel/index.html', context)

class BookingList(ListView):
    model=Booking
    """
    Vamos a mostrar sólo las reservas que estén en el futuro
    Importamos timezone y validamos con gte para que la reserva
    sea mayor o igual al día de la fecha actual
    """

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.filter(check_out__gte=timezone.now()) 
            return booking_list
        else:
            booking_by_user= Booking.objects.filter(user=self.request.user)
            booking_list = booking_by_user.filter(check_out__gte=timezone.now()) 

            return booking_list


class ApartmentDetail(View):

    def get(self, request, *args, **kwargs):

        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        apartment_list= Apartment.objects.filter(category=category)

        if len(apartment_list)>0:
            apartment = apartment_list[0]
            apartment_img = apartment.gallery
            apartment_desc = apartment.description
            apartment_category = dict(apartment.APARTMENT_CATEGORIES).get(apartment.category, None)
            object_list = Booking.objects.all()
            context = {
            'object_list': object_list,
            'apartment_category': apartment_category,
            'form' : form,
            'apartment_img': apartment_img,
            'apartment_desc': apartment_desc
            }
            return render(request, 'apartment_detail.html', context)
        else:
            return HttpResponse('Esa categoría no existe!')


    def post(self, request, *args, **kwargs):

        category = self.kwargs.get('category', None)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
        else:
            return HttpResponse('El formulario tuvo un problema, vuelva a intentarlo.')
        """
        Acá evitamos el reservar para atrás 
        """
        if data['check_in'] > data['check_out']:
            return  HttpResponse('No puedes reservar de esta manera!')  
        """
        Acá evitamos el reservar  el pasado 
        """
        if data['check_in'] < timezone.now().date():
            return  HttpResponse('No puedes reservar el pasado...')  

        apartment_list= Apartment.objects.filter(category=category)

        available_apartments=[]
        for apartment in apartment_list:
            if check_availability(apartment, data['check_in'], data['check_out']):
                available_apartments.append(apartment)
        if len(available_apartments)>0:
            apartment=available_apartments[0]
  
            
            booking= Booking.objects.create(
                user=self.request.user,
                apartment=apartment,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            #return HttpResponse(booking)
            
            return render(request, 'booking_success.html', {'booking': booking})

        else:
            return HttpResponse('Lo sentimos, estos apartamentos están reservados. Pruebe con otro.')

# class BookingView(FormView):
#     form_class=AvailabilityForm
#     template_name='availabiliti_form.html'

class CancelBooking(DeleteView):
    model= Booking
    success_url = reverse_lazy('hotel:BookingList')

class CalendarView(ListView):
    model = Booking
    template_name = 'hotel/calendar.html'
    success_url = reverse_lazy("hotel:calendar")

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
    
    
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     d = get_date(self.request.GET.get('month', None))
#     cal = Calendar(d.year, d.month)
#     html_cal = cal.formatmonth(withyear=True)
#     context['calendar'] = mark_safe(html_cal)
#     context['prev_month'] = prev_month(d)
#     context['next_month'] = next_month(d)
#     return context   