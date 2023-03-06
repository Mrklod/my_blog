from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post
from .forms import PostForm


def main(request):
    context = {
        'title': 'Главная страница',}
    if request.user.is_authenticated:
        author = request.user
        content = Post.objects.filter(author=author)
        context['posts'] = content
    return render(request,'post/main.html',context=context)

def about(request):
    context = {'title': 'О нас'}
    return render(request,'post/about.html',context=context)

def contact(request):
    context = {'title': 'Контакты'}
    return render(request,'post/contact.html',context=context)
@login_required
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
