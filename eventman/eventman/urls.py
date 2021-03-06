"""eventman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from student.views import home,home1,register,comp,lndf,library,cafe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/',home1,name='home1'),
    path('comp/',comp,name='comp'),
    path('lndf/',lndf,name='lndf'),
    path('library/',library,name='Library'),
    path('cafe/',cafe,name='cafe'),
]
