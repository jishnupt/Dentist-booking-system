from django import forms
from .models import CustomUser
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']