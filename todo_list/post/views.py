from django.shortcuts import render
from .models import Post
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
    context = {'title': 'Новый пост'}
    return render(request,'post/new_post.html',context=context)
