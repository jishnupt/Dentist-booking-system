from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegForm,Dr_ProfileForm,BookingForm
from django.contrib.auth import authenticate,login,logout
from .models import Doctor_profile,Book_slot

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def services_page(request):
    return render(request,'services.html')

def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Login_page)
    else:
        form = UserRegForm()
    return render(request,'Register.html',{'form':form})

def AdminRegister(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.role = 'admin'
            data.save()
            return redirect(Login_page)
    else:
        form = UserRegForm()
    return render(request,'AdminReg.html',{'form':form})

def DoctorRegister(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.role = 'doctor'
            data.save()
            Doctor_profile.objects.create(name=data)
            return redirect(Login_page)
    else:
        form = UserRegForm()
    return render(request,'doctorReg.html',{'form':form})

def Dr_profile(request):
    if request.method == 'POST':
        form = Dr_ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(doctor_dashbord)
    else:
        form = Dr_ProfileForm()
    return render(request,'dr_profile.html',{'form':form})

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if user.role == 'admin':
                return redirect(admin_dashbord)
            if user.role == 'patient':
                return redirect(patient_dashbord)
            if user.role == 'doctor':
                return redirect(doctor_dashbord)
            else:
                return HttpResponse('you are not authorized to view this page')
    return render(request,'login.html')

def Logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect(homepage)
    else:
        return render(request,'logout.html')

def admin_dashbord(request):
    return render(request,'admin_page.html')

def patient_dashbord(request):
    drs = Doctor_profile.objects.all()
    return render(request,'patient_page.html',{'drs':drs})

def doctor_dashbord(request):
    return render(request,'doctor_page.html')

def contact_page(request):
    return render(request,'contact.html')

def booking_slots(request,did):
    doct = Doctor_profile.objects.get(id=did)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.userr = request.user
            data.doctr = doct.name
            data.save()
            return redirect(patient_dashbord)
    else:
        form = BookingForm()
    return render(request,'booking_page.html',{'form':form})

def Dr_notification(request):
    Bookings = Book_slot.objects.filter(doctr=request.user)
    return render(request,'Dr_notifi.html',{'Bookings':Bookings})