from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage,name='homepage'),
    path('services_page',services_page,name='services_page'),
    path('RegisterUser',RegisterUser,name='RegisterUser'),
    path('AdminRegister',AdminRegister,name='AdminRegister'),
    path('DoctorRegister',DoctorRegister),
    path('Login_page',Login_page,name='Login_page'),
    path('admin_dashbord',admin_dashbord),
    path('doctor_dashbord',doctor_dashbord),
    path('patient_dashbord',patient_dashbord,name='patient'),
    path('contact_page',contact_page,name='contact'),
    path('Dr_profile',Dr_profile),
    path('Logout_page',Logout_page,name='logout'),
    path('booking_slots/<int:did>',booking_slots,name='booking'),
    path('Dr_notification',Dr_notification,name='Dr_notifi')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)