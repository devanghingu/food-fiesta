from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from django.views.generic import UpdateView,CreateView,ListView,DetailView,DeleteView
from restaurantview.models import Restaurant,Menu,Delivery
from adminview.models import Fooditem,CancelRestaurantRequest
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from foodfiesta.constants import CLOSE,OPEN,ACTIVE,DEACTIVE,PENDING,AVAILABLE,NOT_AVAILABLE
from .forms import ResturantRemoveForm,DeliveryPersonForm

TEMPLATE_PATH = 'backend/restaurantview/'

class Home(View):
    def get(self,request,*args, **kwargs):
        res = Restaurant.objects.filter(user=request.user,parent=None)[0]
        if request.session.get('restaurant') != res.id: 
            messages.success(request,'Welcome '+res.name+' Dashboard ..!')
        request.session['restaurant']=res.id
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
class DashBoard(View):
    ''' Change Dashboard to one branch to another '''
    def get(self,request,*args, **kwargs):
        if Restaurant.objects.filter(id=kwargs.get('pk'),user=request.user).exists():
            res = Restaurant.objects.get(id=kwargs.get('pk'))
            messages.success(request,'Welcome In '+res.name+' Dashboard..!')
            request.session['restaurant']=kwargs.get('pk')
        return render(request,TEMPLATE_PATH+'index.html') 

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


class DeleteRestaurantDeleteView(View):
    ''' Delete Branch Resturant from Menu Using View '''
    def get(self,request,*args, **kwargs):
        res = get_object_or_404(Restaurant,id=kwargs.get('pk'))
        template_name = TEMPLATE_PATH+'pages/product/deleterestaurant.html'
        form = ResturantRemoveForm()
        print('Delete View')
        return render(request,template_name,{'object':res,'form':form})
    
    def post(self,request,*args, **kwargs):
        form = ResturantRemoveForm(request.POST)
        if form.is_valid():
            res = get_object_or_404(Restaurant,id=kwargs.get('pk'))
            reason = form.cleaned_data.get('reason')
            # CancelRestaurantRequest.objects.create(restaurant=res,reason=reason,status=PENDING)
            #HERE Send Email
        if res.id == self.request.session.get('restaurant'):
            return redirect('restaurantview:home') # HERE CHANGE
        Restaurant.objects.filter(id=res.id).update(active=DEACTIVE)
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


# Delivery Person CRUD --start--
class DeliveryList(ListView):
    ''' Menu Of Restaurent Food Listing In Card Using ListView '''
    model         = Delivery
    template_name = TEMPLATE_PATH+'pages/product/deliverylist.html'
    paginate_by   = 8

    def get_queryset(self):
        return Delivery.objects.filter(restaurant=self.request.session.get('restaurant'))
    

class AddDeliveryPersonCreateView(CreateView):
    ''' Delivery Person Create / Add New User and Delivery In Site Using CreateView '''
    form_class    = DeliveryPersonForm
    template_name = TEMPLATE_PATH+'pages/product/adddelivery.html'
    success_url   = reverse_lazy('restaurantview:delivery')
    
    def form_valid(self, form):
        user        = form.save()
        print(user)
        res         = get_object_or_404(Restaurant,id=self.request.session.get('restaurant'))
        Delivery.objects.create(user=user,restaurant=res,status=AVAILABLE)
        messages.success(self.request,'Delivery Person Created Succefully..!')
        return super().form_valid(form)



class DeliveryDetailView(DetailView):
    ''' Delivery person Of Restaurent  Detailt / Description of that Delivery Using DetailView '''
    model         = Delivery
    template_name = TEMPLATE_PATH+'pages/product/deliverytdetail.html'
    
# Delivery--end--  