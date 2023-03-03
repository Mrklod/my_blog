from django.shortcuts import render

# Create your views here.
def register(request):
    context = {'title': 'Регистрация'}
    return render(request,'user/register.html',context=context)

def login(request):
    context = {'title': 'Авторизация'}
    return render(request,'user/login.html',context=context)