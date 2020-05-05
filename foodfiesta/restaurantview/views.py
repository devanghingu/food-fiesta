#django
from django.shortcuts               import redirect, render,get_object_or_404
from django.views                   import View
from django.contrib.messages.views  import SuccessMessageMixin
from django.views.generic           import UpdateView,CreateView,ListView,DetailView,DeleteView
from django.urls                    import reverse_lazy
from django.contrib                 import messages
from django.contrib.auth.models     import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator
#python core
import random

# site specific module
from foodfiesta.constants   import (CLOSE,OPEN,ACTIVE,DEACTIVE,PENDING,AVAILABLE,NOT_AVAILABLE,
                                  PLACED,ACCEPTED,REJECTED,DELIVERED,PREPARED,ORDER_STATUS)
from adminview.models       import Fooditem,CancelRestaurantRequest
from restaurantview.models  import Restaurant,Menu,Delivery
from cart.models            import Order,Orderitem
from accounts.models        import User
from .forms                 import ResturantRemoveForm,DeliveryPersonForm
from .decorators            import check_is_restaurant

#template prefix constant
TEMPLATE_PATH = 'backend/restaurantview/'


#Select Restaurant Dashboard  CRUD --start--
@method_decorator([login_required,check_is_restaurant],name='dispatch')
class SelectDashboard(ListView):
    ''' Menu Of Restaurent Food Listing In Card Using ListView '''
    model         = Restaurant
    template_name = TEMPLATE_PATH+'pages/product/selectdashboard.html'
    paginate_by   = 8

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user,parent=None,active=ACTIVE)


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class AddNewRestaurant(CreateView):
    ''' Add New Restaurent  Create / Add  In Site Using CreateView '''
    model         = Restaurant
    fields        = ('name','address','city','contact','pic')
    template_name = TEMPLATE_PATH+'addnewrestaurant.html'
    success_url   = reverse_lazy('restaurantview:selectdashboard')
    
    def form_valid(self, form):
        restaurant        = form.save(commit=False)
        restaurant.user   = self.request.user 
        restaurant.save()
        messages.success(self.request,'New Resturant Added Succefully..!')
        return super().form_valid(form)

#Select Restaurant Dashboard  CRUD --start--

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class Home(View):
    ''' Render Sub-DashBoard of Home'''
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'index.html') 
        
#Profile / Restaurant CRUD --start--

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class Profile(View):
    def get(self,request,*args, **kwargs):
        return render(request,TEMPLATE_PATH+'pages/product/restaurant-profile.html',{
            'object':Restaurant.objects.get(id=self.request.session.get('restaurant'))
        }) 

#Profile / Restaurant CRUD --end--

#Food / Menu CRUD --start--

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class MenuListView(ListView):
    ''' Menu Of Restaurent Food Listing In Card Using ListView '''
    model         =  Menu
    template_name = TEMPLATE_PATH+'pages/product/foodgrid.html'
    paginate_by   = 8

    def get_queryset(self):
        return Menu.objects.filter(restaurant=self.request.session.get('restaurant'))
    

@method_decorator([login_required,check_is_restaurant],name='dispatch')
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
    

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class FoodDetailView(DetailView):
    ''' Menu Of Restaurent  Detailt / Description of Food Using DetailView '''
    model         = Menu
    template_name = TEMPLATE_PATH+'pages/product/fooddetail.html'


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class DeleteFoodDeleteView(DeleteView):
    ''' Delete Food from Menu Using DeteleView '''
    model         = Menu
    template_name = TEMPLATE_PATH+'pages/product/deletefood.html'
    success_url   = reverse_lazy('restaurantview:menu')


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class EditFoodDeleteView(UpdateView):
    ''' Edit Food Detailt / Description / Price / Quantity of Food Using EditView '''
    model       = Menu
    fields        = ('fooditem','price','available')
    template_name = TEMPLATE_PATH+'pages/product/editfood.html'
    success_url   = reverse_lazy('restaurantview:menu')

# Menu / Food CRUD --end--

# Foositem / NewFood Status CRUD --start--

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class AddFoodItemCreateView(SuccessMessageMixin,CreateView):
    ''' Menu Of Restaurent  Create / Add Food In Menu Using CreateView '''
    model           = Fooditem
    fields          = ('category','name','description','pic')
    template_name   = TEMPLATE_PATH+'pages/product/addfooditem.html'
    success_url     = reverse_lazy('restaurantview:addfood')
    success_message = "Food item add successfully..!"
    

# Fooditem / Newfood Status CRUD --end--


# Order / Order Status CRUD --start--

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class ChangeOrderStatus(View):

    def get(self,request,*args, **kwargs):
        called_page_url = request.META.get('HTTP_REFERER').split('?')[0]
        order = get_object_or_404(Order,id=self.kwargs.get('pk'))
        change_to = {0:PENDING,
                    1:ACCEPTED,
                    2:REJECTED,
                    3:DELIVERED,
                    4:PLACED,
                    5:PREPARED}
                    
        to_status = self.kwargs.get('change_to')
        if to_status == PREPARED:
            delivery_person      = Delivery.objects.filter(restaurant__id=self.request.session.get('restaurant'),status=AVAILABLE)
            if delivery_person.count()>0:
                delivery_person_list   = list(delivery_person.values_list('id',flat=True))
                random_num             = random.randrange(len(delivery_person_list))
                delivery_person        = delivery_person.get(id=delivery_person_list[random_num])
                order.delivery         = delivery_person
                delivery_person.status = NOT_AVAILABLE
                delivery_person.save()
            else:
                messages.error(request,'Delivery Man Not Available Yet!')
                return redirect(called_page_url)

        if to_status == DELIVERED:
            delivery_person         = get_object_or_404(Delivery,id=order.delivery.id)
            delivery_person.status  = AVAILABLE
            delivery_person.save()

        if to_status in change_to.keys():
            order.status=change_to[to_status]
            order.save()   
            messages.success(request,'Order '+dict(ORDER_STATUS)[to_status]+' Successfully..!') 
        return redirect(called_page_url)   


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class OrderPlacedListView(ListView):
    ''' Place Order Of Restaurent Food Listing In Details Using ListView '''
    model         = Order
    template_name = TEMPLATE_PATH+'pages/orderplaced.html'
    paginate_by   = 8

    def get_queryset(self):
        return Order.objects.filter(restaurant__id=self.request.session.get('restaurant'),status=PLACED).order_by('-date')


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class OrderAcceptedListView(ListView):
    ''' Accepted Order Of Restaurent Food Listing In Details Using ListView '''
    model         = Order
    template_name = TEMPLATE_PATH+'pages/orderaccepted.html'
    paginate_by   = 8

    def get_queryset(self):
        return Order.objects.filter(restaurant__id=self.request.session.get('restaurant'),status=ACCEPTED).order_by('-date')


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class OrderPreparedListView(ListView):
    ''' Prepared Order Of Restaurent Food Listing In Details Using ListView '''
    model         = Order
    template_name = TEMPLATE_PATH+'pages/orderprepared.html'
    paginate_by   = 8

    def get_queryset(self):
        return Order.objects.filter(restaurant__id=self.request.session.get('restaurant'),status=PREPARED).order_by('-date')


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class OrderDeliveredListView(ListView):
    ''' Delivered Order Of Restaurent Food Listing In Details Using ListView '''
    model         = Order
    template_name = TEMPLATE_PATH+'pages/orderdelivered.html'
    paginate_by   = 8

    def get_queryset(self):
        return Order.objects.filter(restaurant__id=self.request.session.get('restaurant'),status=DELIVERED).order_by('-date')


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class OrderRejectedListView(ListView):
    ''' Rejected Order Of Restaurent Food Listing In Details Using ListView '''
    model         = Order
    template_name = TEMPLATE_PATH+'pages/orderrejected.html'
    paginate_by   = 8

    def get_queryset(self):
        return Order.objects.filter(restaurant__id=self.request.session.get('restaurant'),status=REJECTED).order_by('-date')


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class Invoice(ListView):
    ''' Details About Order in Invoice Card Using ListView '''
    model         = Orderitem
    template_name = TEMPLATE_PATH+'pages/invoice.html'
    paginate_by   = 8

    def get_queryset(self):
        return self.model.objects.filter(order__restaurant__id=self.request.session.get('restaurant'),order=self.kwargs.get('pk')).order_by('-quantity')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] =Order.objects.get(id=self.kwargs.get('pk')) 
        return context
    
   
# Order / Order Status --end--


#Resturant Views

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class DashBoard(View):
    ''' Change Dashboard to one branch to another '''
    def get(self,request,*args, **kwargs):
        if Restaurant.objects.filter(id=kwargs.get('pk'),user=request.user).exists():
            res = Restaurant.objects.get(id=kwargs.get('pk'))
            messages.success(request,'Welcome In '+res.name+' Dashboard..!')
            request.session['restaurant']=kwargs.get('pk')
        return render(request,TEMPLATE_PATH+'index.html') 


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class ChangeStatusOpenClose(View):

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


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class RestaurantList(ListView):
    ''' Menu Of Restaurent Food Listing In Card Using ListView '''
    model         = Restaurant
    template_name = TEMPLATE_PATH+'pages/product/restaurantlist.html'
    paginate_by   = 8

    def get_queryset(self):
        return Restaurant.objects.filter(parent=self.request.session.get('restaurant'),active=ACTIVE)


    
@method_decorator([login_required,check_is_restaurant],name='dispatch')
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

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class ResturantDetailView(DetailView):
    ''' Branch Of Restaurent  Detailt / Description of that Branch Using DetailView '''
    model         = Restaurant
    template_name = TEMPLATE_PATH+'pages/product/restaurantdetail.html'


@method_decorator([login_required,check_is_restaurant],name='dispatch')
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
            CancelRestaurantRequest.objects.create(restaurant=res,reason=reason,status=PENDING)
            #HERE Send Email
        if res.id == self.request.session.get('restaurant'):
            return redirect('restaurantview:home') # HERE CHANGE
        Restaurant.objects.filter(id=res.id).update(active=DEACTIVE)
        return redirect('restaurantview:restaurant')

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class EditRestaurantUpdateView(SuccessMessageMixin,UpdateView):
    ''' Edit Restaurant and branch Using UpdateView '''
    model           = Restaurant
    fields          = ('name','address','city','contact','pic')
    template_name   = TEMPLATE_PATH+'pages/product/editrestaurant.html'
    success_url     = reverse_lazy('restaurantview:restaurant')
    success_message = 'Restaurant Update Successfully..!'

# Resturant / Restaurant Status --end--

# Customer CRUD --start--

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class Customer(ListView):
    model         = Order
    template_name = TEMPLATE_PATH+'pages/product/customerlist.html'
    paginate_by   = 8

    def get_queryset(self):
        list_user = self.model.objects.filter(restaurant__id=self.request.session.get('restaurant')).values_list('user',flat=True).distinct()    
        return User.objects.filter(id__in=list_user)

# Customer CRUD --end--
# Delivery Person CRUD --start--

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class DeliveryList(ListView):
    ''' Delivery Pesron Listing In Tabel Using ListView '''
    model         = Delivery
    template_name = TEMPLATE_PATH+'pages/product/deliverylist.html'
    paginate_by   = 8

    def get_queryset(self):
        return Delivery.objects.filter(restaurant=self.request.session.get('restaurant'))
    

@method_decorator([login_required,check_is_restaurant],name='dispatch')
class AddDeliveryPersonCreateView(CreateView):
    ''' Delivery Person Create / Add New User and Delivery In Site Using CreateView '''
    form_class    = DeliveryPersonForm
    template_name = TEMPLATE_PATH+'pages/product/adddelivery.html'
    success_url   = reverse_lazy('restaurantview:delivery')
    
    def form_valid(self, form):
        user          = form.save()
        print(user)
        group,created = Group.objects.get_or_create(name='delivery_group')
        res           = get_object_or_404(Restaurant,id=self.request.session.get('restaurant'))
        Delivery.objects.create(user=user,restaurant=res,status=AVAILABLE)
        messages.success(self.request,'Delivery Person Created Succefully..!')
        group.user_set.add(user)
        return super().form_valid(form)


@method_decorator([login_required,check_is_restaurant],name='dispatch')
class DeliveryDetailView(DetailView):
    ''' Delivery person Of Restaurent  Detailt / Description of that Delivery Using DetailView '''
    model         = Delivery
    template_name = TEMPLATE_PATH+'pages/product/deliverydetail.html'
    
# Delivery--end--  
#Delivery Dashboard
class DeliveryHome(ListView):
    model = Order
    template_name = TEMPLATE_PATH+'deliverydashboard.html'
    def get_context_data(self, **kwargs):
        context = super(DeliveryHome,self).get_context_data(**kwargs)
        context['order'] = Order.objects.filter(delivery__user= self.request.user).order_by('status')
        context['user'] = Delivery.objects.filter(user=self.request.user)
        return context

class MarkAsDelivered(View):
    def get(self,request,*args, **kwargs):
        id = kwargs['pk']
        order = get_object_or_404(Order,id=id)
        order.status = DELIVERED
        delivery_person = order.delivery
        delivery_person.status = AVAILABLE
        delivery_person.save()
        order.save()
        messages.success(request,'Order Marked As Delivered')
        return redirect('restaurantview:deliveryhome')
    
class ChangeStatus(View):
    def get(self,request,*args, **kwargs):
        id = kwargs['pk']
        user = get_object_or_404(Delivery,id=id)
        if user.status == True:
            user.status = False
            user.save()
            messages.success(request,"Change Status To Not Availabel")
        else:
            user.status = True
            user.save()
            messages.success(request,"Change Status To Availabel")
        return redirect('restaurantview:deliveryhome')
    