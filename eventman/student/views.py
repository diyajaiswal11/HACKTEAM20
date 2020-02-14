from django.shortcuts import render,redirect,render_to_response
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request,'main.html')

def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']

#         if password1==password2:
#             user=User.objects.create_user(username=username,email=email,password1=password1,password2=password2)
#             user.save()
#             print('User created')
#             return redirect('/')
#     # else:
    return render(request,'register.html')

def login_view(request):
    return render(request, 'login.html')

def home1(request):
    return render(request,'welcome.html')

def comp(request):
    return render(request,'comp.html')

def lndf(request):
    return render(request,'lndf.html')

def event(request):
    return render(request,'event.html')

def cafe(request):
    return render(request,'cafe.html')

