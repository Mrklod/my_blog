from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import FormRegister,FormLogin


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = FormRegister(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = FormRegister()
    context = {'title': 'Регистрация','form':form}
    return render(request,'user/register.html',context=context)



def login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = FormLogin()
    context = {'title': 'Авторизация','form':form}
    return render(request,'user/login.html',context=context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

