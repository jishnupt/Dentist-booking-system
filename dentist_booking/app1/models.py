from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)

    ROLE_CHOICE = (
        ('admin','admin'),
        ('patient','patient'),
        ('doctor','doctor')
    )
    role = models.CharField(max_length=50,choices=ROLE_CHOICE,default='patient')

class Doctor_profile(models.Model):
    name = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    SPECILASATION = [
        ('General Checkup','General Checkup'),
        ('Teeth cleaning','Teeth cleaning'),
        ('Teeth Whitening','Teeth Whitening'),
        ('Root Canal','Root Canal'),
        ('Dental Implants','Dental Implants'),
        ('Emergency Care','Emergency Care')
    ]
    specilaiz = models.CharField(choices=SPECILASATION,default='General Checkup')
    Dr_image = models.ImageField(upload_to='Doctors')

class Book_slot(models.Model):
    userr = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user')
    doctr = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='doctor')
    note = models.TextField(blank=True)
    booking_date = models.DateField()
    
    
    def clean(self):
        if self.booking_date < timezone.now().date():
            raise ValidationError("Booking date cannot be in the past")
