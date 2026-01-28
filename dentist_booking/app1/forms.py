from django import forms
from .models import CustomUser,Doctor_profile,Book_slot
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']

class Dr_ProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor_profile
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Book_slot
        fields = [ 'booking_date', 'note']
        widgets = {
            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': timezone.now().date()
                }
            )
        }

    def clean_booking_date(self):
        date = self.cleaned_data['booking_date']
        if date < timezone.now().date():
            raise forms.ValidationError("You cannot select a past date")
        return date
