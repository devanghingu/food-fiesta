from django.db import models

class City(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name        = models.CharField(max_length=75)
    description = models.TextField(blank=True,null=True)
    pic         = models.ImageField(upload_to='category/',blank=True,null=True)

    def __str__(self):
        return self.name

class Fooditem(models.Model):
    category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    name        = models.CharField(max_length=75)
    description = models.TextField(blank=True,null=True)
    pic         = models.ImageField(upload_to='fooditem/',blank=True,null=True)

    def __str__(self):
        return self.name
