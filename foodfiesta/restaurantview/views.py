from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView,CreateView,ListView,DetailView,DeleteView
from restaurantview.models import Restaurant,Menu
from django.urls import reverse_lazy
from django.contrib import messages

TEMPLATE_PATH = 'backend/restaurantview/'

class Home(View):
    def get(self,request,*args, **kwargs):
        request.session['restaurant']=Restaurant.objects.get(user=request.user).id
        return render(request,TEMPLATE_PATH+'index.html') 

class Profile(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurant-profile.html') 

#Food / Menu CRUD --start--

class MenuListView(ListView):
    ''' Menu Of Restaurent Food Listing In Card Using ListView '''
    model         =  Menu
    template_name = TEMPLATE_PATH+'pages/product/foodgrid.html'
    paginate_by   = 8

    def get_queryset(self):
        return Menu.objects.filter(restaurant=self.request.session.get('restaurant'))
    

class AddFoodCreateView(CreateView):
    ''' Menu Of Restaurent  Create / Add Food In Menu Using CreateView '''
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


# Order / Order Status CRUD --start--

class Order(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/orders.html') 


class Invoice(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/invoice.html') 

# Order / Order Status --end--


#Resturant Views
class RestaurantList(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurantlist.html')


class EditRestaurantUpdateView(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/editrestaurant.html')

        
class RestaurantDetail(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurantdetail.html')

class Customer(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/customerlist.html')

class Delivery(View):

    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/customerlist.html')
        
