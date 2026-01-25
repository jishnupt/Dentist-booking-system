from django.shortcuts import render,redirect
from .forms import UserRegForm

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

def Login_page(request):
    return render(request,'login.html')