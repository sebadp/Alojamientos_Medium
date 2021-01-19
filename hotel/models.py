from django.db import models
from django.conf import settings
# Create your models here.

class Apartment(models.Model):
    ROOM_CATEGORIES=(
        ('COMPARTIDA', 'COMPARTIDA'),
        ('SIN AIRE ACONDICIONADO', 'SIN AIRE ACONDICIONADO'),
        ('SEMI ACONDICIONADO', 'SEMI ACONDICIONADO'),
        ('AIRE ACONDICIONADO', 'AIRE ACONDICIONADO'),
         
    )
    number=models.IntegerField()
    category=models.CharField(max_length=25, choices=ROOM_CATEGORIES)
    rooms=models.IntegerField()
    beds=models.IntegerField()
    capacity=models.IntegerField()
    kitchen=models.BooleanField(default=False)
    garden=models.BooleanField(default=False)
    barbecue=models.BooleanField(default=False)
    garage=models.BooleanField(default=False)
    precio=models.IntegerField()
    description=models.CharField(max_length=500)
    front_img=models.ImageField()
    gallery=models.ImageField()

    def __str__(self):
        return f' {self.number} : {self.category} tiene {self.beds} camas para alojar a {self.capacity} personas.'

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in=models.DateField(("Ingreso"), auto_now=False, auto_now_add=False)
    check_out=models.DateField(("Egreso"), auto_now=False, auto_now_add=False)
    breakfast=models.BooleanField(default=True)
    adults=models.IntegerField()
    kids=models.IntegerField()
    cars=models.IntegerField()
    total=models.IntegerField()

    def __str__(self):
        return f' {self.user} ha reservado {self.apartment} desde {self.check_in} hasta {self.check_out}'