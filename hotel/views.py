from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import Apartment, Booking
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability
from django.urls import reverse

# Create your views here.

# class ApartmentList(ListView):
#     model=Apartment
def ApartmentList(request):
    apartment= Apartment.objects.all()[0]
    apartment_categories = dict(apartment.APARTMENT_CATEGORIES)
    # print('categories', apartment_categories)
    apartment_values= apartment_categories.values()
    # print('values', apartment_values)

    apartment_list=[]
    for apartment_category in apartment_categories:
        apartment= apartment_categories.get(apartment_category)
        apartment_url= reverse('hotel:ApartmentDetail', kwargs={'category': apartment_category})
        # print(apartment, apartment_url)
        apartment_list.append((apartment, apartment_url))
    context={'apartment_list': apartment_list}
    return render(request, 'apartment_list.html', context)

class BookingList(ListView):
    model=Booking

class ApartmentDetail(View):

    def get(self, request, *args, **kwargs):

        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        apartment_list= Apartment.objects.filter(category=category)

        if len(apartment_list)>0:
            apartment = apartment_list[0]
            apartment_category = dict(apartment.APARTMENT_CATEGORIES).get(apartment.category, None)
            context = {
            'apartment_category': apartment_category,
            'form' : form,
            }
            return render(request, 'apartment_detail.html', context)
        else:
            return HttpResponse('Esa categoría no existe!')


    def post(self, request, *args, **kwargs):

        category = self.kwargs.get('category', None)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
        # else:
        #     return HttpResponse('El formulario tuvo un problema, vuelva a intentarlo.')
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
            return HttpResponse(booking)
        else:
            return HttpResponse('Lo sentimos, estos apartamentos están reservados. Pruebe con otro.')

class BookingView(FormView):
    form_class=AvailabilityForm
    template_name='availabiliti_form.html'

