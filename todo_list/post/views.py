from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post
from .forms import PostForm
def main(request):
    content = Post.objects.all()
    context = {
        'title':'Главная страница',
        'posts':content,
    }
    return render(request,'post/main.html',context=context)

def about(request):
    context = {'title': 'О нас'}
    return render(request,'post/about.html',context=context)

def contact(request):
    context = {'title': 'Контакты'}
    return render(request,'post/contact.html',context=context)

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = PostForm()
    context = {'title': 'Новый пост','form':form}
    return render(request,'post/new_post.html',context=context)
