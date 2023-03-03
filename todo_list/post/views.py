from django.shortcuts import render

def main(request):
    return render(request,'post/main.html')

def about(request):
    return render(request,'post/about.html')

def contact(request):
    return render(request,'post/contact.html')

def new_post(request):
    return render(request,'post/new_post.html')