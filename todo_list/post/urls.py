from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('new_post/',new_post,name='new_post'),
]