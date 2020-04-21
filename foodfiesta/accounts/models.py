from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile=models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.first_name
#
# # Admin
# class City(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#
#
# # User
# class Address(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     address = models.TextField(max_length=255)
#     default = models.BooleanField(default=False)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     contact = models.CharField(max_length=13)
#
#
# # Restaurant
# class Restaurant(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     parent = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     fooditem = models.ManyToManyField(Fooditem)
#     name = models.CharField(max_length=75)
#     address = models.TextField(max_length=255)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     contact = models.CharField(max_length=13)
#     open = models.BooleanField(default=False)
#     active = models.BooleanField(default=False)
#     pic = models.ImageField(upload_to='restaurant/')
#
#
# # Admin
# class Category(models.Model):
#     name = models.CharField(max_length=75)
#     description = models.TextField()
#     pic = models.ImageField(upload_to='category/')
#
#
# # Admin
# class Fooditem(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=75)
#     description = models.TextField()
#     pic = models.ImageField(upload_to='fooditem/')
#
#
# # Restaurant
# class Menu(models.Model):
#     fooditem = models.ForeignKey(Fooditem, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     price = models.PositiveIntegerField()
#     available = models.BooleanField(default=False)
#
#
# # Order
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     total_price = models.PositiveIntegerField()
#     status = models.SmallIntegerField()
#     delivery = models.OneToOneField()
#     delivery_status = models.BooleanField()
#
#
# # Order
# class Orderitem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     food = models.ForeignKey(Fooditem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.PositiveIntegerField()
# #Admin
# class City(models.Model):
#     name=models.CharField(max_length=255)
#     description=models.TextField()

#User
class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=255)
    default=models.BooleanField(default=False)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    contact=models.CharField(max_length=13)

# #Restaurant
# class Restaurant(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     parent=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
#     fooditem=models.ManyToManyField(Fooditem)
#     name=models.CharField(max_length=75)
#     address=models.TextField(max_length=255)
#     city=models.ForeignKey(City,on_delete=models.CASCADE)
#     contact=models.CharField(max_length=13)
#     open=models.BooleanField(default=False)
#     active=models.BooleanField(default=False)
#     pic=models.ImageField(upload_to='restaurant/')

# #Admin
# class Category(models.Model):
#     name=models.CharField(max_length=75)
#     description=models.TextField()
#     pic=models.ImageField(upload_to='category/')

# #Admin
# class Fooditem(models.Model):
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)
#     name=models.CharField(max_length=75)
#     description=models.TextField()
#     pic=models.ImageField(upload_to='fooditem/')

#Restaurant
class Menu(models.Model):
    fooditem=models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    available=models.BooleanField(default=False)

#Order
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    date=models.DateTimeField()
    total_price=models.PositiveIntegerField()
    status=models.SmallIntegerField()
    delivery=models.OneToOneField()
    delivery_status=models.BooleanField()

#Order
class Orderitem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    food=models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.PositiveIntegerField()