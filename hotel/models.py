from django.db import models
from datetime import date, datetime
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.

class Apartment(models.Model):
    APARTMENT_CATEGORIES=(
#        ('HOSTEL', 'HOSTEL'),
        ('Saracura', 'Saracura'),
        ('Pa-caa', 'Pa-caa'),
#        ('AIREAC', 'AIRE ACONDICIONADO'),
         
    )
    number=models.IntegerField()
    category=models.CharField(max_length=10, choices=APARTMENT_CATEGORIES)
    rooms=models.IntegerField()
    beds=models.IntegerField()
    capacity=models.IntegerField()
    kitchen=models.BooleanField(default=False)
    garden=models.BooleanField(default=False)
    barbecue=models.BooleanField(default=False)
    garage=models.BooleanField(default=False)
    precio=models.IntegerField()
    description=models.CharField(max_length=500)
    front_img=models.ImageField(upload_to='hotel/static/hotel/images')
    gallery=models.ImageField(upload_to='hotel/static/hotel/images')

    def __str__(self):
        return f' {self.number} : {self.category} tiene {self.beds} camas para alojar a {self.capacity} personas.'

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in=models.DateField(("Ingreso"), auto_now=False, auto_now_add=False)
    check_out=models.DateField(("Egreso"), auto_now=False, auto_now_add=False)
    # breakfast=models.BooleanField(default=True)
    #adults=models.IntegerField()
    #kids=models.IntegerField()
    # cars=models.IntegerField()
    #total=models.IntegerField()

    def __str__(self):
        return f' {self.user} ha reservado {self.apartment} desde {self.check_in} hasta {self.check_out}'
    
    def get_dias(self):
        reserva= (self.check_in - self.check_out) 
        return reserva.days

    def get_total(self):
        precio_unit = self.apartment.precio
        reserva= (self.check_in - self.check_out) 
        total= (reserva.days * precio_unit)
        return total
    
    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBooking', args=[self.pk] )
    
# @property 
# def get_html_url(self):
#     url = reverse('booking_edit', args=(self.id,))  
#     return f'<p>{self.user}</p><a href="{url}">edit</a>'
