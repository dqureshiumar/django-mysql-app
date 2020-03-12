from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length=30, default="")
    img = models.ImageField(upload_to='./pics', default="noimage.jpg")
    desc = models.TextField(default="null")
    price = models.IntegerField(default=500)
    offer = models.BooleanField(default=False)