from django.db import models
from user.models import Users


class Category(models.Model):
    name = models.CharField(max_length=120,unique=True)
    decription = models.TextField()
    actual = models.BooleanField()

class Post(models.Model):
    title = models.CharField(max_length=140,unique=True)
    text = models.TextField()
    author = models.ForeignKey(Users,on_delete=models.CASCADE)