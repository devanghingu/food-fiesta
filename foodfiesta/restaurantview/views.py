from django.shortcuts import render
from django.views import View

TEMPLATE_PATH = 'backend/restaurantview/'

class Home(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'index.html') 

class Profile(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurant-profile.html') 

class Menu(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/foodgrid.html') 

class AddFood(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/addfood.html') 

class FoodDetail(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/fooddetail.html') 


class Order(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/orders.html') 


class Invoice(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/invoice.html') 


#Resturant Views
class Restaurant(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurantlist.html')

class EditRestaurant(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/editrestaurant.html')

        
class RestaurantDetail(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurantdetail.html')
