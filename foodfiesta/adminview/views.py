from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from .forms import *
from cart.models import Orderitem
from restaurantview.models import Restaurant
from django.http import HttpResponse
from django.contrib import messages
from foodfiesta.constants import ACCEPTED,PENDING,REJECTED

# Create your views here.
def home(request):
    return render(request,'adminview/index.html')

class CategoryList(ListView):
    model = Category
    template_name = 'adminview/category/categorygrid.html'

class CategoryDetail(DetailView):
    model = Category
    template_name = 'adminview/category/category_detail.html'

class FoodItemList(ListView):
    model = Fooditem
    template_name = 'adminview/fooditem/fooditemgird.html'

class FoodItemDetail(DetailView):
    model = Fooditem
    template_name = 'adminview/fooditem/fooditem_detail.html'

class CityList(ListView):
    model = City
    template_name = 'adminview/city/citylist.html'


class RestaurantList(ListView):
    model = Restaurant
    template_name = 'adminview/restaurant/restaurantlist.html'


#Category CRUD
class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'adminview/category/category_form.html'

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'adminview/category/category_update.html'
    def get_success_url(self):
            return reverse('adminview:category_detail', kwargs={'pk': self.object.pk})

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'adminview/category/category_confirm_delete.html'
    def get_success_url(self):
            return reverse('adminview:allcategory')

#Restaurant
class Acceptrequest(View):
    def get(self,request,*args,**kwargs):
        id = kwargs['id']
        restaurant = get_object_or_404(Restaurant,id=id)
        if restaurant.active == False:
            restaurant.active = True
            restaurant.save()
            messages.success(request,'Restaurant Activated')
            print("Activated")
        else:
            restaurant.active = False
            restaurant.save()
            print("DeActivated")
            messages.success(request,'Restaurant DeActivated')
        return redirect('adminview:allrestaurant')

class Cancelequest(ListView):
    model = CancelRestaurantRequest
    template_name = 'adminview/restaurant/cancelrequest.html'

class AcceptCancelrequest(View):
    def get(self,request,*args,**kwargs):
        id = kwargs['id']
        restaurant = get_object_or_404(CancelRestaurantRequest,id=id)
        restaurant.status = ACCEPTED
        restaurant.save()
        restaurant.restaurant.delete()
        messages.success(request,"Restaurant Deleted")
        print("Accepted")
        return redirect('adminview:cancelrestaurant')

class Rejectrequest(View):
    def get(self,request,*args,**kwargs):
        id = kwargs['id']
        restaurant = get_object_or_404(CancelRestaurantRequest,id=id)
        restaurant.status = REJECTED
        restaurant.save()
        messages.success(request,"Rejected")
        print("Rejected")
        return redirect('adminview:cancelrestaurant')


#FoodItem CRUD
class FoodItemCreate(CreateView):
    model = Fooditem
    form_class = FoodItemCreateForm
    template_name = 'adminview/fooditem/fooditem_form.html'

class FoodItemUpdate(UpdateView):
    model = Fooditem
    form_class = FoodItemCreateForm
    template_name = 'adminview/fooditem/fooditem_update.html'
    def get_success_url(self):
            return reverse('adminview:fooditem_detail', kwargs={'pk': self.object.pk})

class FoodItemDelete(DeleteView):
    model = Fooditem
    template_name = 'adminview/fooditem/fooditem_confirm_delete.html'
    def get_success_url(self):
            return reverse('adminview:allfooditem')

#FoodItem CRUD
class CityCreate(CreateView):
    model = City
    form_class = CityCreateForm
    template_name = 'adminview/city/city_form.html'
    def get_success_url(self):
            return reverse('adminview:allcity')

class CityUpdate(UpdateView):
    model = City
    form_class = CityCreateForm
    template_name = 'adminview/city/city_update.html'
    def get_success_url(self):
            return reverse('adminview:allcity')

class CityDelete(DeleteView):
    model = City
    template_name = 'adminview/city/city_confirm_delete.html'
    def get_success_url(self):
            return reverse('adminview:allcity')
