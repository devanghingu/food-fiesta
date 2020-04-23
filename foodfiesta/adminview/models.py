from django.db import models
from django.urls import reverse
from foodfiesta.constants import REQUEST_STATUS
from restaurantview.models import Restaurant

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

    def get_absolute_url(self):
        return reverse("adminview:category_detail", kwargs={"pk": self.pk})
    

class Fooditem(models.Model):
    category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    name        = models.CharField(max_length=75)
    description = models.TextField(blank=True,null=True)
    pic         = models.ImageField(upload_to='fooditem/',blank=True,null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("adminview:fooditem_detail", kwargs={"pk": self.pk})
    