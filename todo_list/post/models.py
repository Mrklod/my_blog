
from django.db import models
from user.models import Users


class Category(models.Model):
    name = models.CharField(max_length=120,unique=True)
    decription = models.TextField()
    actual = models.BooleanField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=140,unique=True)
    text = models.TextField()
    author = models.ForeignKey(Users,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,upload_to='post_img')
    time_create = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.title