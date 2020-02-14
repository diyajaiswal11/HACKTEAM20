from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'main.html')

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'reg.html',{'form':form})

def login(request):
    return render(request,'login.html')

@login_required
def home1(request):
    return render(request,'home.html')