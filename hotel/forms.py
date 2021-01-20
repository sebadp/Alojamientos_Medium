from django import forms

class AvailabilityForm(forms.Form):
        # APARTMENT_CATEGORIES=(
        #     ('HOSTEL', 'HOSTEL'),
        #     ('SINAIR', 'SIN AIRE ACONDICIONADO'),
        #     ('SEMIAC', 'SEMI ACONDICIONADO'),
        #     ('AIREAC', 'AIRE ACONDICIONADO'),
        
        # )
        # apartment_category=forms.ChoiceField(choices=APARTMENT_CATEGORIES, required=True)
    check_in=forms.DateField(required=True)
    check_out=forms.DateField(required=True)