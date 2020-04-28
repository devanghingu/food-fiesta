from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import UpdateView,CreateView,ListView,DetailView,DeleteView
from restaurantview.models import Restaurant,Menu
from adminview.models import Fooditem
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from foodfiesta.constants import CLOSE,OPEN,ACTIVE,DEACTIVE
TEMPLATE_PATH = 'backend/restaurantview/'

class Home(View):
    def get(self,request,*args, **kwargs):
        request.session['restaurant']=Restaurant.objects.filter(user=request.user,parent=None)[0].id
        return render(request,TEMPLATE_PATH+'index.html') 

#Profile / Restaurant CRUD --start--

class Profile(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurant-profile.html',{
            'object':Restaurant.objects.get(id=self.request.session.get('restaurant'))
        }) 

#Profile / Restaurant CRUD --end--

#Food / Menu CRUD --start--

class MenuListView(ListView):
    ''' Menu Of Restaurent Food Listing In Card Using ListView '''
    model         =  Menu
    template_name = TEMPLATE_PATH+'pages/product/foodgrid.html'
    paginate_by   = 8

    def get_queryset(self):
        return Menu.objects.filter(restaurant=self.request.session.get('restaurant'))
    

class AddFoodCreateView(CreateView):
    ''' Menu Of Restaurent  Create / Add New Food Item In Site Using CreateView '''
    model         = Menu
    fields        = ('fooditem','price','available')
    template_name = TEMPLATE_PATH+'pages/product/addfood.html'
    success_url   = reverse_lazy('restaurantview:menu')
    
    def form_valid(self, form):
        menu = form.save(commit=False)
        menu.restaurant= Restaurant.objects.get(id=self.request.session.get('restaurant'))
        menu.save()
        messages.success(self.request,'Food Added Succefully..!')
        return super().form_valid(form)
    

class FoodDetailView(DetailView):
    ''' Menu Of Restaurent  Detailt / Description of Food Using DetailView '''
    model         = Menu
    template_name = TEMPLATE_PATH+'pages/product/fooddetail.html'


class DeleteFoodDeleteView(DeleteView):
    ''' Delete Food from Menu Using DeteleView '''
    model         = Menu
    template_name = TEMPLATE_PATH+'pages/product/deletefood.html'
    success_url   = reverse_lazy('restaurantview:menu')

class EditFoodDeleteView(UpdateView):
    ''' Edit Food Detailt / Description / Price / Quantity of Food Using EditView '''
    model       = Menu
    fields        = ('fooditem','price','available')
    template_name = TEMPLATE_PATH+'pages/product/editfood.html'
    success_url   = reverse_lazy('restaurantview:menu')

# Menu / Food CRUD --end--

# Foositem / NewFood Status CRUD --start--

class AddFoodItemCreateView(SuccessMessageMixin,CreateView):
    ''' Menu Of Restaurent  Create / Add Food In Menu Using CreateView '''
    model           = Fooditem
    fields          = ('category','name','description','pic')
    template_name   = TEMPLATE_PATH+'pages/product/addfooditem.html'
    success_url     = reverse_lazy('restaurantview:addfood')
    success_message = "Food item add successfully..!"
    

# Fooditem / Newfood Status CRUD --end--


# Order / Order Status CRUD --start--

class Order(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/orders.html') 


class Invoice(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/invoice.html') 

# Order / Order Status --end--


#Resturant Views

class ChangeStatus(View):

    def get(self,request,*args, **kwargs):
        resaurant = Restaurant.objects.get(id=self.request.session.get('restaurant')) # HERE CHANGE
        if resaurant.open:
            resaurant.open = CLOSE
            messages.success(request,'Restaurant Close Successfull..!')
        else:
            resaurant.open = OPEN
            messages.success(request,'Restaurant Open Successfull..!')
        resaurant.save()
        return redirect('restaurantview:profile')

class RestaurantList(ListView):
    ''' Menu Of Restaurent Food Listing In Card Using ListView '''
    model         = Restaurant
    template_name = TEMPLATE_PATH+'pages/product/restaurantlist.html'
    paginate_by   = 8

    def get_queryset(self):
        return Restaurant.objects.filter(parent=self.request.session.get('restaurant'),active=ACTIVE)


    
class AddRestaurantCreateView(CreateView):
    ''' Menu Of Restaurent  Create / Add New Food Item In Site Using CreateView '''
    model         = Restaurant
    fields        = ('name','address','city','contact','pic')
    template_name = TEMPLATE_PATH+'pages/product/addrestaurant.html'
    success_url   = reverse_lazy('restaurantview:restaurant')
    
    def form_valid(self, form):
        restaurant        = form.save(commit=False)
        restaurant.parent = Restaurant.objects.get(id=self.request.session.get('restaurant'))
        restaurant.user   = self.request.user 
        restaurant.save()
        messages.success(self.request,'Branch Added Succefully..!')
        return super().form_valid(form)

class ResturantDetailView(DetailView):
    ''' Branch Of Restaurent  Detailt / Description of that Branch Using DetailView '''
    model         = Restaurant
    template_name = TEMPLATE_PATH+'pages/product/restaurantdetail.html'


class DeleteRestaurantDeleteView(DeleteView):
    ''' Delete Branch Resturant from Menu Using DeteleView '''
    model         = Restaurant
    template_name = TEMPLATE_PATH+'pages/product/deleterestaurant.html'
    success_url   = reverse_lazy('restaurantview:restaurant')

    def delete(self,request,*args, **kwargs):
        """ Call Sending Delete Restaurant request."""
        self.object = self.get_object()
    
        if self.object.id == self.request.session.get('restaurant'):
            return redirect('restaurantview:home') # HERE CHANGE
        Restaurant.objects.filter(id=self.object.id).update(active=DEACTIVE)
        return redirect('restaurantview:restaurant')


class EditRestaurantUpdateView(SuccessMessageMixin,UpdateView):
    ''' Edit Restaurant and branch Using UpdateView '''
    model           = Restaurant
    fields          = ('name','address','city','contact','pic')
    template_name   = TEMPLATE_PATH+'pages/product/editrestaurant.html'
    success_url     = reverse_lazy('restaurantview:restaurant')
    success_message = 'Restaurant Update Successfully..!'

class Customer(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/customerlist.html')

class Delivery(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/customerlist.html')
        
