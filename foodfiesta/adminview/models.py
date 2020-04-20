from django.db import models

class City(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()

class Category(models.Model):
    name=models.CharField(max_length=75)
    description=models.TextField()
    pic=models.ImageField(upload_to='category/')

class Fooditem(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=75)
    description=models.TextField()
    pic=models.ImageField(upload_to='fooditem/')
    