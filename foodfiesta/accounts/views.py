from accounts.models import User
from adminview.models import City
from allauth.account.forms import SignupForm
from allauth.account.views import LoginView
from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import View
from restaurantview.models import Restaurant

from . import forms


# Create your views here.
class Index(TemplateView):
    """template for display when user come"""

    template_name = "frontend/index.html"


class CustomLoginView(LoginView):
    template_name = "account/login.html"

    def post(self,request,*args,**kwargs):
        response=super().post(request,*args,**kwargs)
        if request.user.groups.filter(name='staff_group').exists():
            if Restaurant.objects.filter(user=request.user,parent=None,active=True):
                print('stafffffffffff')
                return redirect('restaurantview:home')
            else:
                messages.info(request, "Your Restaurant request is in process")
                return redirect('accounts:index')
                
        elif request.user.groups.filter(name='delivery_group').exists():
            print('deliveryyyyyy')
            return redirect('restaurantview:deliveryhome')
        elif request.user.groups.filter(name='user_group').exists():
            print('userrrrrrr')
        elif self.request.user.is_superuser:
            print("Supeeeeeeeeeeeeeeeeerrrrrrrrrrrrrr")
            return redirect('adminview:adminview_home')
        return response

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({"signup_form": SignupForm})

        return context


@method_decorator(login_required, name="dispatch")
class CreateRestaurant(View):
    def get(self, request, *args, **kwargs):
        form = forms.createrestaurant()
        context = {}
        context = {"form": form}
        return render(request, "frontend/createrestaurant.html", context)

    def post(self, request, *args, **kwargs):
        form = forms.createrestaurant(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            city = City.objects.get(id=data["city"])
            name = form.cleaned_data.get("name")
            address = form.cleaned_data.get("address")
            contact = form.cleaned_data.get("contact")
            if Restaurant.objects.filter(name=name).exists():
                messages.info(request, "Restaurant is already Exist")
                return render(request,
                              "frontend/createrestaurant.html",
                              context={"form": form})
            else:
                Restaurant.objects.create(
                    user=request.user,
                    city=city,
                    name=name,
                    address=address,
                    contact=contact,
                )
                new_group, created = Group.objects.get_or_create(
                    name="staff_group")
                alice_group = User.groups.through.objects.get(
                    user=request.user)
                alice_group.group = new_group
                alice_group.save()
                messages.success(request, "New Restaurant Added")
                return redirect("accounts:index")
        else:
            return render(request,
                          "frontend/createrestaurant.html",
                          context={"form": form})
