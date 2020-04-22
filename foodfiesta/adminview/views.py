from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from .forms import *

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
